# Workflows

### TOC

* [Codebase Details](#details)
* [Interfaces & Data Shapes](#interfaces--data-shapes)
* [Workflows](#workflows-interfaces--data-shapes)
  * [Required Data Preparation](#required-data-preparation)
  * [Workflow: Discovery Report](#worklow-discovery-report)
  * [Workflow: Pre-Assembly](#worklow-pre-assembly)
  * [Workflow: Remediation Framework](#worklow-remediation-framework)

![overview diagram](https://docs.google.com/drawings/d/e/2PACX-1vR8X5NbWjdxiw7K5OKEGlj0t4TrK5_IxcU-2LzDMf3Ph5wpS2FFQf68rBf5xqHezLqPxjuo4JcQNoR3/pub?w=2271&h=1494)
[Link to diagram in Google Drawings](https://docs.google.com/drawings/d/11snoNlCLLUEjI1onYC0TqlY-2PqeJhp7QuqBeJK1KIQ/edit?usp=sharing)

## Details

### Dor Workflow Service

- Codebase: https://github.com/sul-dlss/dor-workflow-service
- Logs:
  - default: `workflow_service.log`
- Docs: [Consul Space, Needs updates, conflates with Workfow-Service](https://consul.stanford.edu/pages/viewpage.action?title=DOR+services&spaceKey=DOR#DORservices-initialize_workflow)
- Used in:
  - Anything calling `Dor`?

### Workflow Service

  - Codebase: https://github.com/sul-dlss/workflow-service
  - Machine: lyberservices-[prod|test]
  - Location: `/home/lyberadmin/apps/workflow`
  - Mount:
  - Service URL: https://lyberservices-prod.stanford.edu/workflow/
  - Logs: `home/logs/wfservice.log`
  - Monitoring:
  - Docs: [Consul Space, Needs updates, conflates with Workfow-Service](https://consul.stanford.edu/pages/viewpage.action?title=DOR+services&spaceKey=DOR#DORservices-initialize_workflow)
  - Dependencies:
    - Java 6
    - Oracle 11g
    - Apache Ant
    - Tomcat 6


## Interfaces & Data Shapes

To be made into tests, profiling, or monitoring concerns.

TBD

## Workflows, Interfaces & Data Shapes

### Required Data Preparation


### Worklow:
