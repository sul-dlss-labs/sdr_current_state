# SDR Current State Working Group Work Plan
### Summer 2017

The SDR & DOR ecosystem groupings are largely artificial, for the sake of planning work, and can probably be contested in other contexts.

Note: this will change as needed, and we will keep this plan up to date with the current status.

## Work Plan

Work through the following groupings with these questions in mind:
- in an end-to-end workflow, what object(s) are consumed, what object(s) are produced, and which applications are involved?
- what logging, profiling, or object QA validation checks exist for this segment of the process?
- enumerate the interfaces and connecting processes

1. Object Current State stats: Christina, Tony
    * DOR Fedora 3
    * Pres-Core filesystem
    * Argo Index
    * SURI identifiers numbers
    * PURL-fetcher output
2. Ingest / Entry Points: Ben, Peter, Laura for first two; Tony Calvano
    * Pre-assembly (what uses pre-assembly scripts?)
    * Staging file systems?
    * (separate group) Hydrus &/or ETDs: Cathy, Justin?
    * WAS (was-registrar)
3. DOR Services: Peter, Joe possibly for workflows
    * DOR Services (Gem)
    * DOR Services (App)
    * SURI
    * DOR Workflow Service (Ruby interface to Java)
    * Workflow Service (Java)
    * Fedora 3
4. Robots: Darren H., Ben, Peter
    * Robots Master, Lyber Core, Robot Controller
    * Assembly & Common Accessioning
    * Other Robot Suites
5. Argo+: John M., Tommy, Darren H.?, Peter?, Ben
    * Argo
    * dor_indexing_app
    * sul-mq
    * modsulator
    * (Fedora 3, Solr+)
6. Preservation Core: Darren W., Ben?, Cam, John M.
    * MOAB (Gem)
    * SDR-Preservation Core
    * SDR-Services-App
    * Archive-Catalog (?)
    * SDR-PC File System written to Tape
7. PURL+: Tommy, John M., Naomi
    * PURL / PURL-fetcher
    * Stacks
    * Wowza
7. Indexing, Access & Discovery: Jack, Jesse
    * Discovery Dispatcher
    * sw-indexer
    * sul-embed
    * SearchWorks
    * Spotlight
8. Wrap-up / Overview of State

## SDR Ecosystem Overview Groupings

![overview image](https://docs.google.com/drawings/d/1qMBtEHv2pnka2kPd5IB9m03nG24Sq4orxyQWbpJdgyI/pub?w=1440&h=1080)

## Back-lot Ideas or Questions

Back-lot of ideas raised for work steps/output, kept for future referral:

- "scriptware"?
- IIIF publishing relationships to SDR ecosystem
- Spotlight inclusion? Out of scope for this?
