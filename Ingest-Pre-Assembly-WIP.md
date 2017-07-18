# Ingest: Pre-Assembly

![overview diagram](https://docs.google.com/drawings/d/e/2PACX-1vR8X5NbWjdxiw7K5OKEGlj0t4TrK5_IxcU-2LzDMf3Ph5wpS2FFQf68rBf5xqHezLqPxjuo4JcQNoR3/pub?w=2271&h=1494)

## Details

- Codebase: https://github.com/sul-dlss/pre-assembly
- Machine: `sul-lyberservices-[test|prod]`
- Location: `/home/lyberadmin/pre-assembly/current`
- Mount(s): `/dor/content`
- Logs:
  - project-specific: some in `/dor/preassembly`; others in project specific directories;
  - code-specific: `current/log/`
- Monitoring: [Honeybadger (Not currently monitoring anything)](https://app.honeybadger.io/projects/52900/faults?q=-is%3Aresolved+-is%3Aignored)
- Docs: Consul Space (Mostly Up-To-Date)

## Interfaces & Data Shapes

### Preparatory

- User creates in workspace for each Collection or Project:
  - [Configuration YAML file](https://github.com/sul-dlss/pre-assembly/blob/master/config/projects/TEMPLATE.yaml)
    - ```YAML
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
  - CSV Manifest
  - Descriptive Metadata template
  - Objects Directory w/Access

- Materials location + access (required)
- If objects are registered:
    - If not, Manifest as CSV with sourceid, filename, label is required
    - If using Manifest, MODS XML template (optional)
- Descriptive metadata location + access (optional)
- Materials Folder structure  - keep or don’t
- Project's APO DRUID (required)
- Associated Dor Set Object’s APO DRUID (optional)
