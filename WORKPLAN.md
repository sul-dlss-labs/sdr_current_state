# SDR Current State Working Group Work Plan
### Summer 2017

The SDR & DOR ecosystem groupings are largely artificial, for the sake of planning work, and can probably be contested in other contexts.

Note: this will change as needed, and we will keep this plan up to date with the current status.

## Work Plan

Work through the following groupings with these questions in mind:
- in an end-to-end workflow, what object(s) are consumed, what object(s) are produced, and which applications are involved?
- what logging, profiling, or object QA validation checks exist for this segment of the process?
- enumerate the interfaces and connecting processes

2. ~Ingest / Entry Points~
    * [Pre-assembly (what uses pre-assembly scripts)](Ingest-Pre-Assembly.md)
    * [Hydrus](Ingest-Hydrus.md)
    * [ETDs](Ingest-ETDs.md)
    * [WAS (was-registrar)](Ingest-WAS.md)
    * Staging file systems
3. ~DOR Services~
    * [DOR Services (Gem)](Dor-Services-Gem.md)
    * [DOR Services (App)](Dor-Services-App.md)
    * [SURI](SURI.md)
    * [DOR Workflow Service (Ruby interface to Java)](Dor-Workflow-Service.md)
    * [Workflow Service (Java)](Workflow-Service.md)
    * Fedora 3
4. Robots
    * [Robots Master, Lyber Core, Robot Controller](Robots.md)
    * [Assembly](Robots-Assembly.md)
    * [Common Accessioning](Robots-Common-Accessioning.md)
    * [Other Robot Suites](Robot-Suites.md)
      * Item Release
      * ETD Robots
      * Gis robot suite
      * Goobi Robot
      * Dor gsb robots
      * Sdr Pres Core Robots
      * WAS Robot Suite
      * WAS Metadata Extractor
    * [Workflows Details](Robots-Workflows-Details.md)
7. PURL+: Tommy, Naomi, Chris B.
    * [PURL](PURL.md)
    * [PURL-fetcher](PURL-fetcher.md)
    * [Stacks](PURL-Stacks.md)
    * [Wowza](Wowza.md)
5. Argo+: John M., Tommy, Peter?, Ben
    * [Argo](Argo.md)
    * [SUL MQ (Messaging)](SUL-MQ.md)
    * [Dor Indexing App](Dor-Indexing-App.md)
    * [Dor Camel Routes](Dor-Camel-Routes.md)
    * [Modsulator](Modsulator.md)
    * [Modsulator Rails App](Modsulator-Rails-App.md)
1. Object Current State stats: Christina, Tony
    * DOR Fedora 3
    * Pres-Core filesystem
    * Argo Index
    * SURI identifiers numbers
    * PURL-fetcher output
6. Preservation Core: Darren W., Ben?, Kam, John M.
    * MOAB (Gem)
    * SDR-Preservation Core
    * SDR-Services-App
    * Archive-Catalog (?)
    * SDR-PC File System written to Tape
7. Access & Discovery: Jack, Jessie, geo-Darren
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
