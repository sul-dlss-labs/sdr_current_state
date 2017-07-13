import requests
from argparse import ArgumentParser
import json
import time

"https://sul-solr.stanford.edu/solr/argo3_prod/select?"


def get_total(base_url):
    """Get & return the total number of document via open query to Solr."""
    try:
        resp = requests.get(base_url)
        print(base_url)
        resp.raise_for_status()
        resp = resp.json()
        total = resp['response']['numFound']
        return(total)
    except requests.exceptions.Timeout:
        time.sleep(1)
        get_total(base_url)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


def get_docs(base_url, pages, output_file):
    """Get & append the JSON docs from open query to Solr to output_file."""
    for page in range(1232, pages):
        doc_url = base_url + "&rows=1000&start=" + str(page)
        print("Attempting page %d download" % (page))
        try:
            resp = requests.get(doc_url).json()
            for doc in resp['response']['docs']:
                with open(output_file, 'a') as fh:
                    json.dump(doc, fh)
                    fh.write(',\n')
        except requests.exceptions.Timeout:
            time.sleep(1)
            try:
                resp = requests.get(doc_url).json
                for doc in resp['response']['docs']:
                    with open(output_file, 'a') as fh:
                        json.dump(doc, fh)
                        fh.write(',\n')
            except requests.exceptions.RequestException as e:
                print(e)
                pass
        except requests.exceptions.RequestException as e:
            print(e)
            pass


def main():
    parser = ArgumentParser(usage='%(prog)s [options]')
    parser.add_argument("-u", "--url", dest="base_url", help="Solr Query URL.")
    parser.add_argument("-o", "--out", dest="out_file", help="Out JSON file.")

    args = parser.parse_args()

    if not args.base_url and not args.out_file:
        parser.print_help()
        exit()

    call_url = args.base_url + "indent=on&q=*:*&wt=json"
    total = get_total(call_url)
    pages = int(total / 1000) + (total % 1000 > 0)
    # with open(args.out_file, 'w') as out:
    #   out.write('{"docs": [')
    # with open(args.out_file, 'a') as out:
    #     out.write(',')
    print("Working through %d Solr Documents over %d Pages." % (total, pages))
    get_docs(call_url, pages, args.out_file)
    with open(args.out_file, 'a') as out:
        out.write(']}')


if __name__ == '__main__':
    main()
