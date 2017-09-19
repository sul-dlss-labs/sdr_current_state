# Ingest: Pre-Assembly

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

- Codebase: https://github.com/sul-dlss/pre-assembly
- Machine: `sul-lyberservices-[test|prod]`
- Location: `/home/lyberadmin/pre-assembly/current`
- Mount(s): `/dor/content`
- Logs:
  - project-specific: some in `/dor/preassembly`; others in project specific directories;
  - code-specific: `current/log/`
- Monitoring: [Honeybadger (Not currently monitoring anything)](https://app.honeybadger.io/projects/52900/faults?q=-is%3Aresolved+-is%3Aignored)
- Docs: [Consul Space (Mostly Up-To-Date)](https://consul.stanford.edu/display/chimera/Automated+Accessioning+and+Object+Remediation+%28pre-assembly+and+assembly%29)
- Dependencies:
  - `Fedora 3 (DOR Fedora) via ActiveFedora/Dor-Services (gem)`
  - `SUL Solr argo_prod3 Index`
  - `DOR-Services-App`
    - `/objects/{druid}/apo_workflows/assemblyWF`
    - `/suri2/namespaces/druid`
  - Check local gems needed in Gemfile.lock

## Interfaces & Data Shapes

To be made into tests, profiling, or monitoring concerns.

TBD

## Workflows, Interfaces & Data Shapes

### Required Data Preparation

User creates the following in workspace for each Collection or Project:
  - [Configuration YAML file (REQUIRED)](https://github.com/sul-dlss/pre-assembly/blob/master/config/projects/TEMPLATE.yaml)
    ```YAML
        project_name:      'Foo'                   # Required. Used as prefix to sourceID and as project tag if registering objects.
        progress_log_file: ~                       # Optional.
        apo_druid_id: 'druid:aa111bb2222'          # Required if pre-assembly is registering the objects.
        set_druid_id: 'druid:yy888xx9999'          # Pre-assembly will associate the object with a set in Dor.
        validate_files: true                       # image files confirmed as valid before proceeding (mimetype & have color profiles)
                        false                      # no image validation performed.
        project_style:
          content_structure: 'simple_image'        # <contentMetadata type="image"> and <resource type="image">
                             'file'                # <contentMetadata type="file"> and <resource type="file">.
                             'simple_book'         # <contentMetadata type="book"> and <resource type="page">.
                             'book_with_pdf'       # any file other than an image (e.g. a PDF) will have <resource type="file">
                             'book_as_image'       # <contentMetadata type="book"> and <resource type="image"> instead of "page".
                             'smpl'                # Used for SMPL projects
          content_tag_override:   false            # DEFAULT if not supplied -- content_structure as defined above is always used
                                  true             # content_structure type is determined from registered object content type tag
          should_register: true
                           false
          apply_tag:      'prefix : tagname : etc' # only applicable if "should_register" is set to true
          get_druid_from: 'suri'                   # Only used with should_register = true.
                          'container'              # Object is contained in a druid subdirectory
                          'container_barcode'      # Object is contained in a barcode subdirectory. Druid fetched from a service.
                          'manifest'               # Object's druid is in a column in the manifest called "druid".
                          'druid_minter'           # Mints a mock druid rather than using Suri.  Development purposes.
        bundle_dir: '/foo/bar/revs'                # Input location for the project content (i.e., the "bundle").
        staging_dir: ~                             # Where to put the pre-assembled materials. Where the assembly robots expect to find content.
        staging_style: 'copy'                      # Staging style, can be "copy" or "symlink", defaults to "copy" if not specified or nil
        object_discovery:
          # Option 1: use a manifest.
          use_manifest: true                       # Set glob and regex to nil.
                        false                      # Set glob and regex parameters to match your sub-directories
          # Option 2: two-phase directory crawl.
          glob: '*'                                # Everything.
                '*.tif'                            # Only .tif files.
          regex: ~                                 # No filtering.
                 '^[a-z][a-z]\d\d\d[a-z][a-z]\d\d\d\d$'   # Only druid directories.
                 '^\d+$'                                  # Only barcode directories.

        stageable_discovery:
          # Option 1: If you set 'use_container' to true, this will simply stage the entire object directory that was matched above.
          use_container: true                      # If true , set glob and regex to nil below.
                         false                     # If false, use glob and regex below.

          # Option 2: If you set 'use_container' to false, staging done via a two-phase container crawl based on patterns below.
          glob:  '0[12]/'                          # Stage the 00, 01, and 02 subdirectories.
                 '00/*'                            # Stage the items in the 00 subdirectory only, but not the '00' folder itself.
                 '*/*'                             # Stage the items residing at the second level in the structure.
                 '**/*'                            # Stage all leaf items. Results it total flattening.
                 '*'                               # Stage all items at the root level of the container
          regex:  ~                                # No filtering.
                 '(?ix) \. (tif|xml) $'            # Stage only items with .tif and .xml extentions.
          files_only: true                         # if set to true, then only files will be staged, regardless of glob specified above
        accession_items:   ~                       # Only valid for projects that do *not* use a manifest.
          only:
            - 'aa111aa1111'
            - 'bb222bb2222'                        # this is an example of two objects that will be accessioned
          except:
            - 'aa111aa1111'
            - 'bb222bb2222'                        # this is an example of two objects that will be ignored
          reaccession: true                        # If running a re-accession, set this to true so that a cleanup will be performed
        manifest:         'manifest.csv'           # The manifest file, if 'use_manifest' is true.
        checksums_file:   'checksums.txt'          # A provider checksum file (in default md5sum format).
        desc_md_template: 'mods_template.xml'      # An optional descriptive metadata XML template to use with manifest.
        manifest_cols:
          object_container:   'filename'           # Required, column name containing the filename (single file per object) or folder.
          source_id:          'sourceid'           # Required if project_style:should_register = true
          label:              'label'              # Required if project_style:should_register = true
        content_exclusion: ~                       # Include all staged files in content metadata.
                           '(?i)\.xml$'            # Exclude xml files from content metadata.
        content_md_creation:
          style: 'default'
                 'filename'                        # Collects files together into a single resource based on filename
                 'dpg'                             # Collects files together into a single resource based on DPG filenaming convention
                 'smpl'                            # Generate a content metadata file using the SMPL preContentMetadata.
                 'none'                            # Do not generate any contentMetadata.xml file.
          smpl_manifest: 'smpl_manifest.csv'       # The manifest file for use in SMPL projects.
        publish_attr:  ~                           # If not specified, will be added by the assembly robots based on mimetype.
          shelve:     'no'
          publish:    'no'
          preserve:   'yes'
          'image/jp2':
            publish:  'yes'
            shelve:   'yes'
            preserve: 'no'
          'image/tiff':
            publish:  'no'
            shelve:   'no'
            preserve: 'yes'
          'default':
            publish:  'no'
            shelve:   'no'
            preserve: 'yes'
        resume: false                              # If true, pre-assembly skips objects already successfully pre-assembled, as indicated by progress_log_file.
        limit_n: ~                                 # Set to an integer if you want to process only a limited number of the discovered objects.
        init_assembly_wf: true                     # Whether pre-assembly should initiate the assembly workflow for the object.
        throttle_time:  ~                          # The number of seconds to sleep between each object.
        new_druid_tree_format:  true               # Determines druid tree directory format (defaults to "true").
        compute_checksum: true                     # Whether pre-assembly should compute checksums.
        validate_usage: true                       # Whether pre-assembly should confirm that all expected YAML parameters have been supplied.
        show_progress: true                        # Whether to print druids as they are pre-assembled on the command line.
        uniqify_source_ids: false                  # If true, pre-assembly attached a timestamp to source IDs.
        cleanup: false                             # If true, pre-assembly deletes objects from DOR after pre-assembly finishes.
        profile: false                             # NOT CURRENTLY WORKING
        garbage_collect_each_n:  50                # manually run garbage collection each time this number of objects is pre-assembled
        validate_bundle_dir:
          code:   '/some/full/path/to/validation_code.rb'
          report: '/some/full/path/to/validation_warnings.csv'
    ```
  - [CSV Manifest (OPTIONAL, location given in YAML)](https://raw.githubusercontent.com/sul-dlss/pre-assembly/master/config/projects/manifest_template/TEMPLATE_manifest.csv)
    ```CSV
       format,sourceid,filename,label,year,inst_notes,prod_notes,has_more_metadata,description
       "BW film","foo-2.2","image3.tif","Avus 1938, 1956","1938, 1956","strip 2 is duplicate; don't scan","","","this is a description"
    ```
  - [Descriptive Metadata template (OPTIONAL, location given in YAML)](https://github.com/sul-dlss/pre-assembly/blob/master/config/projects/manifest_template/TEMPLATE_mods.xml)
    ```XML
    <?xml version="1.0"?>
    <mods xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.loc.gov/mods/v3" version="3.3" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-3.xsd">
      <typeOfResource>still image</typeOfResource>
      <genre authority="att">digital image</genre>
      <subject authority="lcsh">
        <topic>Collection/Project Subject Heading 1</topic>
        <topic>Collection/Project Subject Heading 2</topic>
      </subject>
      <relatedItem type="host">
        <titleInfo>
          <title>Collection / Project Title</title>
        </titleInfo>
        <typeOfResource collection="yes"/>
      </relatedItem>
      <relatedItem type="original">
        <physicalDescription>
          <form authority="att">[[format]]</form>
        </physicalDescription>
      </relatedItem>
      <originInfo>
        <dateCreated>[[year]]</dateCreated>
      </originInfo>
      <titleInfo>
        <% if manifest_row[:label] %>
    	    <title>[[label]]</title>
      <% end %>
      </titleInfo>
      <% if manifest_row[:description] %>
        <note>
          <%=manifest_row[:description]%>
        </note>
      <% end %>
      <identifier type="local" displayLabel="Revs ID">
        [[sourceid]]
      </identifier>
      <% if manifest_row[:inst_notes] %>
        <note type="source note" ID="inst_notes">
          <%=manifest_row[:inst_notes]%>
        </note>
      <% end %>
      <% if manifest_row[:prod_notes] %>
        <note type="source note" ID="prod_notes">
          <%=manifest_row[:prod_notes]%>
        </note>
      <% end %>
      <% if manifest_row[:has_more_metadata] %>
        <note type="source note" ID="has_more_metadata">
          <%=manifest_row[:has_more_metadata]%>
        </note>
      <% end %>
    </mods>
    ```

### Worklow: Discovery Report
User on sul-lyberservices-[test|prod] & in `pre-assembly/current` runs `bin/discovery_report [confirm_checksums|check_sourceids|no_check_reg|show_staged|show_smpl_cm]`:
   - `Pre-Assembly::Bundle` Object instantiated with @params == YAML file read into memory
     - Reads `AssemblyUtils::Assembly` @Assembly_Workspace
   - `PreAssembly::Reporting.discovery_report(@params)`
     - Checks @apo_druid_id from params with `Assembly::Utils.is_apo?()`
     - Calls `Dor::Item.find(druid)` for @apo_druid_id
     - Calls `ActiveFedora.find(id)` for @apo_druid_id
     - **Queries Fedora**, returns AF Object
     - Checks `obj.identityMetadata.objectType.first == 'adminPolicy'` for the AF Object
     - Calls `PreAssembly::Bundle.discover_objects`
       - `PreAssembly::DigitalObject` Object instantiated
       - Digital Object data attributes added:
         ```
         @pid = ''
         @druid = nil
         @dor_object = nil
         @reg_by_pre_assembly = false
         @label = Dor::Config.dor.default_label
         @source_id = nil
         @manifest_row = nil
         @content_md_file = contentMetadata.xml (at root of object directory)
         @technical_md_file = descMetadata.xml (at root of object directory)
         @desc_md_file = technicalMetadata.xml (at root of object directory)
         @content_md_xml = ''
         @technical_md_xml = ''
         @desc_md_xml = ''
         @pre_assem_finished = false
         @content_structure  = @project_style
         ```
    - For each digital object in the generated array of objects:
      - Passes @barcode to `PreAssembly::DigitalObject.get_pid_from_container_barcode()`
        - Passes barcode to `Dor::SearchService.query_by_id`
        - Queries **SUL Solr argo_prod3 Index**, returns DRUIDs for Objects
      - Passes returned pids to `PreAssembly::DigitalObject.get_dor_item_apos(pid)`
        - Passes each pid to `Dor::Item.find(pid)`
        - **Queries Fedora**, returns AF Object
      - Then passes @source_id for checking to `Assembly::Utils.get_druids_by_sourceid(source_ids)`
        - Passes barcode to `Dor::SearchService.query_by_id`
        - Queries **SUL Solr argo_prod3 Index**, returns DRUIDs for Objects
        - Checks the response size == 0
  - `PreAssembly::Reporting.discovery_report(params)` completes with report out to STDOUT
    - See data output for the report here: https://github.com/sul-dlss/pre-assembly/blob/b46edb09f3ed45df54e5685cd8230d8104d504dd/lib/pre_assembly/reporting.rb#L192

### Worklow: Pre-Assembly
User on sul-lyberservices-[test|prod] & in `/home/lyberadmin/pre-assembly/current` runs `OBOT_ENVIRONMENT=env nohup bin/pre-assemble OPTS YAML_FILE`:
   - params = YAML file, then add
     - params['resume'] = true if options[resume]
     - params['limit_n'] = options[limit].to_i if options[limit]
     - params['config_filename'] = YAML_FILE
   - `Pre-Assembly::Bundle` Object instantiated with @params
     - Reads `AssemblyUtils::Assembly` @Assembly_Workspace
   - `PreAssembly::Bundle.run_pre_assembly()`
     - Does special work if SMPL Object / Manifest
     - Calls `PreAssembly::Bundle.discover_objects`
       - `PreAssembly::DigitalObject` Object instantiated
       - Digital Object data attributes added:
         ```
         @pid = ''
         @druid = nil
         @dor_object = nil
         @reg_by_pre_assembly = false
         @label = Dor::Config.dor.default_label
         @source_id = nil
         @manifest_row = nil
         @content_md_file = contentMetadata.xml (at root of object directory)
         @technical_md_file = descMetadata.xml (at root of object directory)
         @desc_md_file = technicalMetadata.xml (at root of object directory)
         @content_md_xml = ''
         @technical_md_xml = ''
         @desc_md_xml = ''
         @pre_assem_finished = false
         @content_structure  = @project_style
         ```
    - For each digital object in the generated array of objects:
       - Reads the checksums stored with the Objects
       - Adds fields from the provided Manifest
       - Calls `PreAssembly::Bundle.process_digital_objects`
         - `desc_md_template_xml` passed to `PreAssembly::DigitalObject.pre_assemble(desc_md_xml)`
           - Calls `PreAssembly::DigitalObject.determine_druid()`, depending on @params['project_style']['get_druid_form']:
             - `get_pid_from_manifest`
               - Retrieves `manifest_row[druid]` from provided Manifest
             - `get_pid_from_suri`
               - Calls `Dor::SuriService.mint_id`
               - Issues POST Request to **DOR-Services-App /suri2/namespaces/druid**
             - `get_pid_from_druid_minter`
               - Calls `PreAssembly::DruidMinter.next()` for testing only
             - `get_pid_from_container`
               - Retrieves data from params['container_basename']
             - `get_pid_from_container_barcode`
               - Passes @barcode to `PreAssembly::DigitalObject.get_pid_from_container_barcode()`
                 - Passes barcode to `Dor::SearchService.query_by_id`
                 - Queries **SUL Solr argo_prod3 Index**, returns DRUIDs for Objects
             - Returns a DRUID
           - Calls `PreAssembly::DigitalObject.prepare_for_reaccession`
             - Passes `druid,[:stacks,:stage,:symlinks]` to `AssemblyUtils.cleanup_object`
             - Cleans up Pre-assembly Staging
           - Passes `registration_params` to `PreAssembly::DigitalObject.register_in_dor(params)`
             - Passes `registration_params` to `Dor::RegistrationService.register_object params`
             - Calls `Dor::RegistrationService.register_object()`
             - **Updates Fedora** and returns AF Object
             - If there is an error with the Fedora call, check that something doesn't already exist:
               - Passes `source_id` to `Dor::SearchService.query_by_id`
                 - **Queries SUL Solr argo_prod3 Index**
               - Passes `pid` to `Dor::SearchService.delete_by_id(pid)` to delete the PID created if already existed
               - Calls `Dor::SearchService.solr.commit`
                 - **Updates SUL Solr argo_prod3 Index**
           - Calls `PreAssembly::DigitalObject.add_object_to_set()`
             - Adds `[:is_member_of, "info:fedora/#{setID}"]`, `[:is_member_of_collection, "info:fedora/#{setID}"]` to Object
             - Calls Object.save (**Fedora via ActiveFedora via Dor::Item?**)
           - Calls `PreAssembly::DigitalObject.stage_files()`
           - Calls `PreAssembly::DigitalObject.generate_content_metadata()`
             - Calls `Assembly::ContentMetadata.create_content_metadata`
           - Calls `PreAssembly::DigitalObject.generate_technical_metadata()`
           - Calls `PreAssembly::DigitalObject.generate_desc_metadata()`
           - Calls `PreAssembly::DigitalObject.initialize_assembly_workflow()`
             - POST request with no content, auth header to **DOR-Services-App /objects/{druid}/apo_workflows/assemblyWF**
             - Checks status_code response for success
       - Calls `PreAssembly::Bundle.delete_digital_objects`
         - Deletes digital objects if development environment
         - Returns to stdout any errors
   - Profiling saved to memory_report.txt
   - Array of processed PIDs returned to STDOUT


### Worklow: Remediation Framework

TBD
