import requests
from argparse import ArgumentParser
import json
import time

"https://purl-fetcher-prod.stanford.edu/purls"


def get_total(base_url):
    """Get & return the total number of document via open query to /purls."""
    try:
        resp = requests.get(base_url)
        resp.raise_for_status()
        resp = resp.json()
        total = resp['pages']['total_pages']
        return(total)
    except requests.exceptions.Timeout:
        time.sleep(1)
        get_total(base_url)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


def get_docs(base_url, pages, output_file):
    """Get & append the JSON docs from open query to /purls to output_file."""
    for page in range(8479, pages):
        doc_url = base_url + "?page=" + str(page)
        print("Attempting page %d download" % (page))
        try:
            resp = requests.get(doc_url).json()
            for purl in resp['purls']:
                with open(output_file, 'a') as out:
                    json.dump(purl, out)
                    out.write(',\n')
        except requests.exceptions.RequestException as e:
            print(e)
            pass


def main():
    parser = ArgumentParser(usage='%(prog)s [options]')
    parser.add_argument("-u", "--url", dest="base_url", help="PURL API URL.")
    parser.add_argument("-o", "--out", dest="out_file", help="Out JSON file.")

    args = parser.parse_args()

    if not args.base_url and not args.out_file:
        parser.print_help()
        exit()

    call_url = args.base_url + "purls"
    pages = get_total(call_url)
    # with open(args.out_file, 'w') as out:
    #     out.write('{"docs": [')
    # with open(args.out_file, 'a') as out:
    #     out.write(',')
    print("Working through Purl Objects over %d Pages." % (pages))
    get_docs(call_url, pages, args.out_file)
    with open(args.out_file, 'a') as out:
        out.write(']}')


if __name__ == '__main__':
    main()
