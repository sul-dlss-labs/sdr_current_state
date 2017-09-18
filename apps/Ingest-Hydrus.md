# Ingest: Hydrus

### TOC

* [Codebase Details](#details)
* [Interfaces & Data Shapes](#interfaces--data-shapes)
* [Workflows](#workflows-interfaces--data-shapes)
  * [Required Data Preparation](#required-data-preparation)
  * [Workflow: ](#worklow-)

![overview diagram](https://docs.google.com/drawings/d/e/2PACX-1vSLJXuphIH4_La3eYiiPY3zIuc46cJVPBQ2w_OKA2mmq0vqR0CIt6kZmGpQQhl_SCSL13kdNHobmuZI/pub?w=5364&h=2534)
[Link to diagram in Google Drawings](https://docs.google.com/drawings/d/1f2nuhSlG7Ct2RZLYZTHZduHuEPQTg2Rq9BW0IG_VbcQ/edit?usp=sharing)

## Details

- Codebase: https://github.com/sul-dlss/hydrus/
- Machine: `hydrus-[test|prod].stanford.edu`
- Location: `/home/lyberadmin/hydrus/current`
- GUI: http://sdr.stanford.edu
- Mount(s):
  - Mount point for NFS: `/data/hydrus-files`
  - Mount serves files from `sf3-webapp:/vol/hydrus_files_[test|prod]`
- Hydrus MySQL: `/var/lib/mysql/hydrus/`
- Hydrus Solr Collection: [SUL Solr Hydrus Collection](https://sul-solr.stanford.edu/solr/#/hydrus/)
- Logs: `/home/lyberadmin/hydrus/current/log/` (except `workflow_service.log`, which is ..)
- Monitoring: [Honeybadger](https://app.honeybadger.io/projects/49897/faults?q=)
- Docs:
  - [Consul Space (Mostly Up-To-Date)]()
  - [Codebase Readme - OUT OF DATE]()
- Dependencies:
  - `Fedora 3 (DOR Fedora) via ActiveFedora/Dor-Services (gem)`
  - Dor::WorkflowService (gem)
  - `SUL Solr Hydrus Collection Index`
  - `DOR-Services-App`
    - `/v1/objects/#{pid}/publish`
  - Check local gems needed in Gemfile.lock

## Interfaces & Data Shapes

To be made into tests, profiling, or monitoring concerns.

TBD

## Workflows, Interfaces & Data Shapes

### Required Data Preparation

### Worklow:
