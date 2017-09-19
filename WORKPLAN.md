# SDR Current State Working Group Work Plan
### Summer 2017

The SDR & DOR ecosystem groupings are largely artificial, for the sake of planning work, and can probably be contested in other contexts.

Note: this will change as needed, and we will keep this plan up to date with the current status.

## SDR Ecosystem Overview Groupings

![overview image](https://docs.google.com/drawings/d/1qMBtEHv2pnka2kPd5IB9m03nG24Sq4orxyQWbpJdgyI/pub?w=1440&h=1080)

Working folder (has many diagrams and notes in progress): https://drive.google.com/drive/folders/0B74oOQcTdnHjSk4wSS0yWFJLRWs?usp=sharing

## Proposed Outcomes of this Work

1. Dataflow & data model diagrams for shared understanding.
2. Dataflow & data model 'specs' for details useful for data processing, development, dev-ops, or operational concerns about codebases or system-wide / integration-level work.
3. All the updated / gathered ops & dev-ops info being put into devopsdocs or another appropriate identified place.
4. List and details of interfaces and data assessment points we want to log / monitor better.
5. Identifying key components we can more readily move to data pipelines architecture (including ETL processing) across applications.
6. Continuing to build out https://github.com/sul-dlss/docker-sdr based on the interfaces we’re identifying for better application development integration testing.
7. Improved documentation generation for dataflows by development teams.
8. Patch party and possible work cycles for cleaning up & adding better logging, monitoring, analytics & report generation for SDR, based off the findings of this work.

## Work Plan

Work through the following groupings with these questions in mind:
- in an end-to-end workflow, what object(s) are consumed, what object(s) are produced, and which applications are involved?
- what logging, profiling, or object QA validation checks exist for this segment of the process?
- enumerate the interfaces and connecting processes

2. ~Ingest / Entry Points~
    * [Pre-assembly (what uses pre-assembly scripts)](apps/Ingest-Pre-Assembly.md)
    * [Hydrus](apps/Ingest-Hydrus.md)
    * [ETDs](apps/Ingest-ETDs.md)
    * [WAS (was-registrar)](apps/Ingest-WAS.md)
    * Staging file systems
3. ~DOR Services~
    * [DOR Services (Gem)](apps/Dor-Services-Gem.md)
    * [DOR Services (App)](apps/Dor-Services-App.md)
    * [SURI](apps/SURI.md)
    * [DOR Workflow Service (Ruby interface to Java)](apps/Dor-Workflow-Service.md)
    * [Workflow Service (Java)](apps/Workflow-Service.md)
    * Fedora 3
4. Sept. 14 / Robots: geo-Darren
    * [Robots Master, Lyber Core, Robot Controller](apps/Robots.md)
    * [Assembly](apps/Robots-Assembly.md)
    * [Common Accessioning](apps/Robots-Common-Accessioning.md)
    * [Other Robot Suites](apps/Robot-Suites.md)
      * Item Release
      * ETD Robots
      * Gis robot suite
      * Goobi Robot
      * Sdr Pres Core Robots
      * WAS Robot Suite
      * WAS Metadata Extractor
    * [Workflows Details](apps/Robots-Workflows-Details.md)
7. Sept. 21-28 / PURL+: Tommy, Naomi, Chris B.
    * [PURL](apps/PURL.md)
    * [PURL-fetcher](apps/PURL-fetcher.md)
    * [Stacks](apps/PURL-Stacks.md)
    * [Wowza](apps/Wowza.md)
5. Oct. 5-19 / Argo+: John M., Tommy, Peter, Ben
    * [Argo](apps/Argo.md)
    * [SUL MQ (Messaging)](apps/SUL-MQ.md)
    * [Dor Indexing App](apps/Dor-Indexing-App.md)
    * [Dor Camel Routes](apps/Dor-Camel-Routes.md)
    * [Modsulator](apps/Modsulator.md)
    * ~Modsulator Rails App~
1. Oct. 26 / Object Current State stats: Christina, Tony
    * DOR Fedora 3
    * Pres-Core filesystem
    * Argo Index
    * SURI identifiers numbers
    * PURL-fetcher output
6. Nov. 2-16 (no meeting the 9th) / Preservation Core: Darren W., Ben, Kam, John M.
    * MOAB (Gem)
    * SDR-Preservation Core
    * SDR-Services-App
    * Archive-Catalog (?)
    * SDR-PC File System written to Tape
7. Nov. 30 - Dec. 7 / Access & Discovery: Jack, Jessie, geo-Darren
    * Discovery Dispatcher
    * sw-indexer
    * sul-embed
    * SearchWorks
    * Spotlight
8. Dec. 14 / Wrap-up & Overview, Next Steps

## Back-lot Ideas or Questions

Back-lot of ideas raised for work steps/output, kept for future referral:

- "scriptware"?
- IIIF publishing relationships to SDR ecosystem
- Spotlight inclusion? Out of scope for this?
