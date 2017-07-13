# SDR Current Objects

- Fedora 3 (dor-prod)
    - Filesystem: sul-dor-prod.stanford.edu/data / sf6-webapp:/sul_dor_prod_data
		- Database:
- DRUIDs (SURI)
    - Endpoint: http://sul-lyberservices-test|dev|prod.stanford.edu/suri2/namespaces/druid
    - Database: ??
- Stacks
    - Filesystem (items that are shelved): /home/lyberadmin/stacks/
- Preservation Core
    - filesystem:
- Argo Index
    - Solr index:
- SearchWorks Index
    - Solr index, filtered for SDR: Not included at present
- PURL
    - PURL-fetcher: https://purl-fetcher-prod.stanford.edu/purls
		- PURL application database:
		- PURL file system:

Similar code:
- Laney wrote something that audits SearchWorks against Argo (against PURL?)
- SDR-PC Reports are run by Tony, not sure where those report scripts are

Numbers, fields, files

## Argo Index Solr

### Numbers
	- from GUI:
		- item	1,446,421
		- collection	1,586
		- adminPolicy	918
		- set	776
		- agreement	50
		- workflow	23
		- total: 1,449,774 DOR objects
	- from Solr:
		- 1,463,843 total Solr documents
    - active_fedora_model_ssi values:
 - Dor::Item: 1461263,
 - Dor::Collection: 1586,
        - Dor::AdminPolicyObject: 918,
        - Dor::Agreement: 50,
        - Dor::WorkflowObject: 23,
        - Hydrus::AdminPolicyObject: 14

### Fields (Usage to be added)

```
METS_resource_count_itsi: |==                       | 139869/1464000 |   9%
							 _version_: |=========================| 1464000/1464000 | 100%
					abstract_tesim: |=                        | 116492/1464000 |   7%
			accession_tag_ssim: |                         |  14940/1464000 |   1%
			accessioned_dttsim: |================         | 938988/1464000 |  64%
accessioned_earliest_dttsi: |================         | 938988/1464000 |  64%
accessioned_latest_dttsi: |================         | 938988/1464000 |  64%
 active_fedora_model_ssi: |=========================| 1464000/1464000 | 100%
				agreementId_ssim: |==                       | 156115/1464000 |  10%
			 agreementId_tesim: |==                       | 156115/1464000 |  10%
					agreement_ssim: |                         |   1792/1464000 |   0%
apo_register_permissions_ssim: |                         |   1792/1464000 |   0%
apo_register_permissions_tesim: |                         |   1792/1464000 |   0%
apo_role_dor-apo-manager_ssim: |                         |   1792/1464000 |   0%
apo_role_group_dor-apo-manager_ssim: |                         |   1792/1464000 |   0%
apo_role_hydrus-collection-depositor_ssim: |                         |   1792/1464000 |   0%
apo_role_hydrus-collection-manager_ssim: |                         |   1792/1464000 |   0%
apo_role_hydrus-collection-viewer_ssim: |                         |    433/1464000 |   0%
apo_role_person_hydrus-collection-depositor_ssim: |                         |   1792/1464000 |   0%
apo_role_person_hydrus-collection-manager_ssim: |                         |   1792/1464000 |   0%
apo_role_person_hydrus-collection-viewer_ssim: |                         |    433/1464000 |   0%
					apo_title_ssim: |======================   | 1313941/1464000 |  89%
				 apo_title_tesim: |======================   | 1313941/1464000 |  89%
audio_resource_count_itsi: |                         |   8601/1464000 |   0%
				 barcode_id_ssim: |==                       | 163299/1464000 |  11%
					batch_tag_ssim: |                         |  33444/1464000 |   2%
					 book_tag_ssim: |=                        | 113863/1464000 |   7%
				 callseq_id_ssim: |==                       | 140773/1464000 |   9%
					catkey_id_ssim: |===                      | 201443/1464000 |  13%
				 catkey_tag_ssim: |==========               | 620363/1464000 |  42%
	 collection_title_ssim: |=====================    | 1242741/1464000 |  84%
	collection_title_tesim: |=====================    | 1242741/1464000 |  84%
				conforms_to_ssim: |                         |   1434/1464000 |   0%
 content_file_count_itsi: |===============          | 932789/1464000 |  63%
			 content_type_ssim: |===============          | 932789/1464000 |  63%
				coordinates_ssim: |                         |  54746/1464000 |   3%
					copyright_ssim: |===========              | 649386/1464000 |  44%
						 creator_ssi: |======                   | 353141/1464000 |  24%
					 creator_tesim: |======                   | 353141/1464000 |  24%
		 current_version_isi: |=========================| 1464000/1464000 | 100%
				dataset_tag_ssim: |                         |   1921/1464000 |   0%
					dc_creator_ssi: |======                   | 353141/1464000 |  24%
				dc_creator_tesim: |======                   | 353141/1464000 |  24%
dc_identifier_barcode_ssi: |==                       | 141692/1464000 |   9%
dc_identifier_barcode_tesim: |==                       | 141692/1464000 |   9%
dc_identifier_callseq_ssi: |==                       | 140773/1464000 |   9%
dc_identifier_callseq_tesim: |==                       | 140773/1464000 |   9%
dc_identifier_catkey_ssi: |==                       | 142112/1464000 |   9%
dc_identifier_catkey_tesim: |==                       | 142112/1464000 |   9%
 dc_identifier_druid_ssi: |=========================| 1464000/1464000 | 100%
dc_identifier_druid_tesim: |=========================| 1464000/1464000 | 100%
dc_identifier_fuller_ssi: |                         |   3149/1464000 |   0%
dc_identifier_fuller_tesim: |                         |   3149/1464000 |   0%
dc_identifier_google_ssi: |==                       | 140773/1464000 |   9%
dc_identifier_google_tesim: |==                       | 140773/1464000 |   9%
	dc_identifier_isbn_ssi: |                         |    741/1464000 |   0%
dc_identifier_isbn_tesim: |                         |    741/1464000 |   0%
	dc_identifier_issn_ssi: |                         |  17351/1464000 |   1%
dc_identifier_issn_tesim: |                         |  17351/1464000 |   1%
	dc_identifier_lccn_ssi: |=                        |  78110/1464000 |   5%
dc_identifier_lccn_tesim: |=                        |  78110/1464000 |   5%
dc_identifier_mdtoolkit_ssi: |                         |    323/1464000 |   0%
dc_identifier_mdtoolkit_tesim: |                         |    323/1464000 |   0%
dc_identifier_shelfseq_ssi: |==                       | 140773/1464000 |   9%
dc_identifier_shelfseq_tesim: |==                       | 140773/1464000 |   9%
dc_identifier_sulair_ssi: |                         |     66/1464000 |   0%
dc_identifier_sulair_tesim: |                         |     66/1464000 |   0%
	 dc_identifier_uri_ssi: |                         |  15207/1464000 |   1%
 dc_identifier_uri_tesim: |                         |  15207/1464000 |   1%
	dc_identifier_uuid_ssi: |==                       | 149891/1464000 |  10%
dc_identifier_uuid_tesim: |==                       | 149891/1464000 |  10%
						dc_title_ssi: |======================== | 1463414/1464000 |  99%
					dc_title_tesim: |======================== | 1463414/1464000 |  99%
 decommissioned_tag_ssim: |                         |    625/1464000 |   0%
		 default_rights_ssim: |                         |   1792/1464000 |   0%
default_use_license_machine_ssi: |                         |    441/1464000 |   0%
				deposited_dttsim: |=============            | 799135/1464000 |  54%
deposited_earliest_dttsi: |=============            | 799135/1464000 |  54%
	deposited_latest_dttsi: |=============            | 799135/1464000 |  54%
				described_dttsim: |================         | 939890/1464000 |  64%
described_earliest_dttsi: |================         | 939890/1464000 |  64%
	described_latest_dttsi: |================         | 939890/1464000 |  64%
				digitized_dttsim: |                         |  25280/1464000 |   1%
digitized_earliest_dttsi: |                         |  25280/1464000 |   1%
	digitized_latest_dttsi: |                         |  25280/1464000 |   1%
	dissertationid_id_ssim: |                         |  10679/1464000 |   0%
						 dor_id_ssim: |======================== | 1454714/1464000 |  99%
						dor_id_tesim: |======================== | 1454714/1464000 |  99%
dor_services_version_ssi: |=========================| 1464000/1464000 | 100%
						dpg_tag_ssim: |                         |  24905/1464000 |   1%
					druid_tag_ssim: |                         |    130/1464000 |   0%
					 ds_specs_ssim: |=========================| 1464000/1464000 | 100%
						eem_tag_ssim: |                         |   1149/1464000 |   0%
	 embargo_release_dtsim: |                         |   5950/1464000 |   0%
		 embargo_status_ssim: |======================== | 1458259/1464000 |  99%
						etd_tag_ssim: |                         |  10679/1464000 |   0%
		 event_0_message_ssm: |===============          | 908969/1464000 |  62%
				event_0_type_ssm: |===============          | 908969/1464000 |  62%
				event_0_when_ssm: |===============          | 908969/1464000 |  62%
				 event_0_who_ssm: |===============          | 908969/1464000 |  62%
		event_10_message_ssm: |                         |   7963/1464000 |   0%
			 event_10_type_ssm: |                         |   7963/1464000 |   0%
			 event_10_when_ssm: |                         |   7963/1464000 |   0%
				event_10_who_ssm: |                         |   7963/1464000 |   0%
		event_11_message_ssm: |                         |  13497/1464000 |   0%
			 event_11_type_ssm: |                         |  13497/1464000 |   0%
			 event_11_when_ssm: |                         |  13497/1464000 |   0%
				event_11_who_ssm: |                         |  13497/1464000 |   0%
		event_12_message_ssm: |                         |  10944/1464000 |   0%
			 event_12_type_ssm: |                         |  10944/1464000 |   0%
			 event_12_when_ssm: |                         |  10944/1464000 |   0%
				event_12_who_ssm: |                         |  10944/1464000 |   0%
		event_13_message_ssm: |                         |  10377/1464000 |   0%
			 event_13_type_ssm: |                         |  10377/1464000 |   0%
			 event_13_when_ssm: |                         |  10377/1464000 |   0%
				event_13_who_ssm: |                         |  10377/1464000 |   0%
		event_14_message_ssm: |                         |   9026/1464000 |   0%
			 event_14_type_ssm: |                         |   9026/1464000 |   0%
			 event_14_when_ssm: |                         |   9026/1464000 |   0%
				event_14_who_ssm: |                         |   9026/1464000 |   0%
		event_15_message_ssm: |                         |    781/1464000 |   0%
			 event_15_type_ssm: |                         |    781/1464000 |   0%
			 event_15_when_ssm: |                         |    781/1464000 |   0%
				event_15_who_ssm: |                         |    781/1464000 |   0%
		event_16_message_ssm: |                         |   9609/1464000 |   0%
			 event_16_type_ssm: |                         |   9609/1464000 |   0%
			 event_16_when_ssm: |                         |   9609/1464000 |   0%
				event_16_who_ssm: |                         |   9609/1464000 |   0%
		event_17_message_ssm: |                         |   9276/1464000 |   0%
			 event_17_type_ssm: |                         |   9276/1464000 |   0%
			 event_17_when_ssm: |                         |   9276/1464000 |   0%
				event_17_who_ssm: |                         |   9276/1464000 |   0%
		event_18_message_ssm: |                         |   9243/1464000 |   0%
			 event_18_type_ssm: |                         |   9243/1464000 |   0%
			 event_18_when_ssm: |                         |   9243/1464000 |   0%
				event_18_who_ssm: |                         |   9243/1464000 |   0%
		event_19_message_ssm: |                         |   8807/1464000 |   0%
			 event_19_type_ssm: |                         |   8807/1464000 |   0%
			 event_19_when_ssm: |                         |   8807/1464000 |   0%
				event_19_who_ssm: |                         |   8807/1464000 |   0%
		 event_1_message_ssm: |======                   | 400068/1464000 |  27%
				event_1_type_ssm: |======                   | 400068/1464000 |  27%
				event_1_when_ssm: |======                   | 400068/1464000 |  27%
				 event_1_who_ssm: |======                   | 400068/1464000 |  27%
		event_20_message_ssm: |                         |    586/1464000 |   0%
			 event_20_type_ssm: |                         |    586/1464000 |   0%
			 event_20_when_ssm: |                         |    586/1464000 |   0%
				event_20_who_ssm: |                         |    586/1464000 |   0%
		event_21_message_ssm: |                         |    586/1464000 |   0%
			 event_21_type_ssm: |                         |    586/1464000 |   0%
			 event_21_when_ssm: |                         |    586/1464000 |   0%
				event_21_who_ssm: |                         |    586/1464000 |   0%
		event_22_message_ssm: |                         |    436/1464000 |   0%
			 event_22_type_ssm: |                         |    436/1464000 |   0%
			 event_22_when_ssm: |                         |    436/1464000 |   0%
				event_22_who_ssm: |                         |    436/1464000 |   0%
		event_23_message_ssm: |                         |    436/1464000 |   0%
			 event_23_type_ssm: |                         |    436/1464000 |   0%
			 event_23_when_ssm: |                         |    436/1464000 |   0%
				event_23_who_ssm: |                         |    436/1464000 |   0%
		 event_2_message_ssm: |=======                  | 466825/1464000 |  31%
				event_2_type_ssm: |=======                  | 466825/1464000 |  31%
				event_2_when_ssm: |=======                  | 466825/1464000 |  31%
				 event_2_who_ssm: |=======                  | 466825/1464000 |  31%
		 event_3_message_ssm: |=                        | 116610/1464000 |   7%
				event_3_type_ssm: |=                        | 116610/1464000 |   7%
				event_3_when_ssm: |=                        | 116610/1464000 |   7%
				 event_3_who_ssm: |=                        | 116610/1464000 |   7%
		 event_4_message_ssm: |=                        | 106898/1464000 |   7%
				event_4_type_ssm: |=                        | 106898/1464000 |   7%
				event_4_when_ssm: |=                        | 106898/1464000 |   7%
				 event_4_who_ssm: |=                        | 106898/1464000 |   7%
		 event_5_message_ssm: |==                       | 175300/1464000 |  11%
				event_5_type_ssm: |==                       | 175300/1464000 |  11%
				event_5_when_ssm: |==                       | 175300/1464000 |  11%
				 event_5_who_ssm: |==                       | 175300/1464000 |  11%
		 event_6_message_ssm: |==                       | 135832/1464000 |   9%
				event_6_type_ssm: |==                       | 135832/1464000 |   9%
				event_6_when_ssm: |==                       | 135832/1464000 |   9%
				 event_6_who_ssm: |==                       | 135832/1464000 |   9%
		 event_7_message_ssm: |                         |  51165/1464000 |   3%
				event_7_type_ssm: |                         |  51165/1464000 |   3%
				event_7_when_ssm: |                         |  51165/1464000 |   3%
				 event_7_who_ssm: |                         |  51165/1464000 |   3%
		 event_8_message_ssm: |                         |  47011/1464000 |   3%
				event_8_type_ssm: |                         |  47011/1464000 |   3%
				event_8_when_ssm: |                         |  47011/1464000 |   3%
				 event_8_who_ssm: |                         |  47011/1464000 |   3%
		 event_9_message_ssm: |                         |  41119/1464000 |   2%
				event_9_type_ssm: |                         |  41119/1464000 |   2%
				event_9_when_ssm: |                         |  41119/1464000 |   2%
				 event_9_who_ssm: |                         |  41119/1464000 |   2%
			 event_message_ssm: |===============          | 908969/1464000 |  62%
					event_type_ssm: |===============          | 908969/1464000 |  62%
					event_when_ssm: |===============          | 908969/1464000 |  62%
					 event_who_ssm: |===============          | 908969/1464000 |  62%
			 exploded_tag_ssim: |======================== | 1455523/1464000 |  99%
						 extent_ssim: |===============          | 896161/1464000 |  61%
file_resource_count_itsi: |                         |  52973/1464000 |   3%
	first_shelved_image_ss: |============             | 724162/1464000 |  49%
		google_book_tag_ssim: |==                       | 140773/1464000 |   9%
					has_model_ssim: |=========================| 1464000/1464000 | 100%
	 hydrus_apo_title_ssim: |                         |   6811/1464000 |   0%
	hydrus_apo_title_tesim: |                         |   6811/1464000 |   0%
hydrus_collection_title_ssim: |                         |   5168/1464000 |   0%
hydrus_collection_title_tesim: |                         |   5168/1464000 |   0%
											id: |=========================| 1464000/1464000 | 100%
				 identifier_ssim: |=========================| 1464000/1464000 | 100%
				identifier_tesim: |=========================| 1464000/1464000 | 100%
image_resource_count_itsi: |==========               | 608877/1464000 |  41%
				imageqced_dttsim: |                         |   1066/1464000 |   0%
imageqced_earliest_dttsi: |                         |   1066/1464000 |   0%
	imageqced_latest_dttsi: |                         |   1066/1464000 |   0%
				 imported_dttsim: |                         |  25311/1464000 |   1%
 imported_earliest_dttsi: |                         |  25311/1464000 |   1%
	 imported_latest_dttsi: |                         |  25311/1464000 |   1%
				 indexed_at_dtsi: |=========================| 1464000/1464000 | 100%
				inprocess_dttsim: |                         |   2410/1464000 |   0%
inprocess_earliest_dttsi: |                         |   2410/1464000 |   0%
	inprocess_latest_dttsi: |                         |   2410/1464000 |   0%
	is_constituent_of_ssim: |==                       | 156738/1464000 |  10%
		is_dependent_of_ssim: |                         |   5588/1464000 |   0%
		 is_governed_by_ssim: |======================   | 1313941/1464000 |  89%
is_member_of_collection_ssim: |=====================    | 1242741/1464000 |  84%
			 is_member_of_ssim: |=====================    | 1240468/1464000 |  84%
				 is_part_of_ssim: |                         |   1493/1464000 |   0%
					 jira_tag_ssim: |                         |  26238/1464000 |   1%
						lab_tag_ssim: |=                        | 101048/1464000 |   6%
					 label_id_ssim: |===========              | 678970/1464000 |  46%
					lifecycle_ssim: |======================== | 1454677/1464000 |  99%
main-augmented_resource_count_itsi: |                         |  10679/1464000 |   0%
main-original_resource_count_itsi: |                         |  10679/1464000 |   0%
					 maps_tag_ssim: |                         |    436/1464000 |   0%
				 mdform_tag_ssim: |                         |   1910/1464000 |   0%
		metadata_format_ssim: |=========================| 1464000/1464000 | 100%
metadata_resource_count_itsi: |==                       | 139869/1464000 |   9%
		 metadata_source_ssi: |=========================| 1464000/1464000 | 100%
	 modified_latest_dttsi: |=========================| 1464000/1464000 | 100%
		mods_identifier_ssim: |=============            | 816319/1464000 |  55%
	 mods_identifier_tesim: |=============            | 816319/1464000 |  55%
mods_typeOfResource_ssim: |=====================    | 1288259/1464000 |  87%
mods_typeOfResource_tesim: |=====================    | 1288259/1464000 |  87%
						mus_tag_ssim: |                         |      6/1464000 |   0%
nonhydrus_apo_title_ssim: |======================   | 1307130/1464000 |  89%
nonhydrus_apo_title_tesim: |======================   | 1307130/1464000 |  89%
nonhydrus_collection_title_ssim: |=====================    | 1237573/1464000 |  84%
nonhydrus_collection_title_tesim: |=====================    | 1237573/1464000 |  84%
	 obj_create_date_tesim: |=========================| 1464000/1464000 | 100%
obj_diss_index_view_url_ssim: |=========================| 1464000/1464000 | 100%
obj_diss_index_view_url_tesim: |=========================| 1464000/1464000 | 100%
obj_item_index_view_url_ssim: |=========================| 1464000/1464000 | 100%
obj_item_index_view_url_tesim: |=========================| 1464000/1464000 | 100%
					obj_label_ssim: |======================== | 1463558/1464000 |  99%
				 obj_label_tesim: |======================== | 1463558/1464000 |  99%
 obj_last_mod_date_tesim: |=========================| 1464000/1464000 | 100%
				 obj_models_ssim: |=========================| 1464000/1464000 | 100%
				obj_models_tesim: |=========================| 1464000/1464000 | 100%
			 obj_owner_id_ssim: |=========================| 1464000/1464000 | 100%
			obj_owner_id_tesim: |=========================| 1464000/1464000 | 100%
obj_rights_locations_ssim: |                         |   2675/1464000 |   0%
					obj_state_ssim: |=========================| 1464000/1464000 | 100%
				 obj_state_tesim: |=========================| 1464000/1464000 | 100%
			objectCreator_ssim: |======================== | 1453565/1464000 |  99%
		 objectCreator_tesim: |======================== | 1453565/1464000 |  99%
					 objectId_ssim: |======================== | 1454714/1464000 |  99%
				 objectType_ssim: |======================== | 1454714/1464000 |  99%
			object_profile_ssm: |=========================| 1464000/1464000 | 100%
object_resource_count_itsi: |==                       | 118456/1464000 |   8%
				object_state_ssi: |=========================| 1464000/1464000 | 100%
					 opened_dttsim: |========                 | 494858/1464000 |  33%
	 opened_earliest_dttsi: |========                 | 494858/1464000 |  33%
		 opened_latest_dttsi: |========                 | 494858/1464000 |  33%
originInfo_0_date_created_tesim: |==============           | 874258/1464000 |  59%
originInfo_0_place_0_placeTerm_tesim: |=========                | 544316/1464000 |  37%
originInfo_0_place_1_placeTerm_tesim: |===                      | 184376/1464000 |  12%
originInfo_0_place_2_placeTerm_tesim: |                         |  10388/1464000 |   0%
originInfo_0_publisher_tesim: |====                     | 287590/1464000 |  19%
originInfo_1_date_created_tesim: |                         |  42639/1464000 |   2%
originInfo_1_place_0_placeTerm_tesim: |                         |    617/1464000 |   0%
originInfo_1_publisher_tesim: |                         |   7475/1464000 |   0%
originInfo_2_date_created_tesim: |                         |    113/1464000 |   0%
originInfo_2_publisher_tesim: |                         |     30/1464000 |   0%
originInfo_3_publisher_tesim: |                         |     30/1464000 |   0%
originInfo_date_created_tesim: |==============           | 877070/1464000 |  59%
originInfo_place_placeTerm_tesim: |============             | 726543/1464000 |  49%
originInfo_publisher_tesim: |=====                    | 294415/1464000 |  20%
page_resource_count_itsi: |====                     | 257379/1464000 |  17%
permissions_resource_count_itsi: |                         |   2588/1464000 |   0%
				pipelined_dttsim: |                         |   8123/1464000 |   0%
pipelined_earliest_dttsi: |                         |   8123/1464000 |   0%
	pipelined_latest_dttsi: |                         |   8123/1464000 |   0%
		preserved_size_dbtsi: |===============          | 932789/1464000 |  63%
preview_resource_count_itsi: |                         |   1921/1464000 |   0%
				process_tag_ssim: |=============            | 784501/1464000 |  53%
processing_status_code_isi: |=========================| 1464000/1464000 | 100%
processing_status_text_ssi: |=========================| 1464000/1464000 | 100%
				project_tag_ssim: |=====================    | 1259500/1464000 |  86%
public_dc_relation_tesim: |=====================    | 1242741/1464000 |  84%
				published_dttsim: |================         | 939023/1464000 |  64%
published_earliest_dttsi: |================         | 939023/1464000 |  64%
	published_latest_dttsi: |================         | 939023/1464000 |  64%
referencesAgreement_ssim: |                         |   1792/1464000 |   0%
	registered_by_tag_ssim: |============             | 735953/1464000 |  50%
			 registered_dttsim: |============             | 756994/1464000 |  51%
registered_earliest_dttsi: |============             | 756994/1464000 |  51%
 registered_latest_dttsi: |============             | 756994/1464000 |  51%
			release_date_dtsim: |                         |   5950/1464000 |   0%
				 released_dttsim: |                         |   1303/1464000 |   0%
 released_earliest_dttsi: |                         |   1303/1464000 |   0%
	 released_latest_dttsi: |                         |   1303/1464000 |   0%
				released_to_ssim: |====                     | 234295/1464000 |  16%
	remediated_by_tag_ssim: |===============          | 906878/1464000 |  61%
		 resource_count_itsi: |===============          | 932789/1464000 |  63%
		 resource_types_ssim: |===============          | 932789/1464000 |  63%
rights_characteristics_ssim: |======================== | 1463375/1464000 |  99%
rights_descriptions_ssim: |=========================| 1464000/1464000 | 100%
			rights_errors_ssim: |                         |   2409/1464000 |   0%
			rights_primary_ssi: |=========================| 1464000/1464000 | 100%
						 rights_ssim: |=========================| 1464000/1464000 | 100%
							scale_ssim: |=                        |  85406/1464000 |   5%
					scanned_dttsim: |                         |   7980/1464000 |   0%
	scanned_earliest_dttsi: |                         |   7980/1464000 |   0%
		scanned_latest_dttsi: |                         |   7980/1464000 |   0%
									 score: |=========================| 1464000/1464000 | 100%
				 series_tag_ssim: |                         |  32297/1464000 |   2%
				shelfseq_id_ssim: |==                       | 140773/1464000 |   9%
shelved_content_file_count_itsi: |===============          | 932789/1464000 |  63%
					 smpl_tag_ssim: |                         |  18485/1464000 |   1%
					source_id_ssim: |======================== | 1430085/1464000 |  97%
							status_ssi: |=========================| 1464000/1464000 | 100%
subject_0_geographic_ssim: |===                      | 198652/1464000 |  13%
subject_0_geographic_tesim: |===                      | 198652/1464000 |  13%
subject_0_temporal_tesim: |                         |  22457/1464000 |   1%
		subject_0_topic_ssim: |==============           | 856958/1464000 |  58%
	 subject_0_topic_tesim: |==============           | 856958/1464000 |  58%
subject_10_geographic_ssim: |                         |    273/1464000 |   0%
subject_10_geographic_tesim: |                         |    273/1464000 |   0%
	 subject_10_topic_ssim: |                         |   4840/1464000 |   0%
	subject_10_topic_tesim: |                         |   4840/1464000 |   0%
subject_11_geographic_ssim: |                         |    469/1464000 |   0%
subject_11_geographic_tesim: |                         |    469/1464000 |   0%
	 subject_11_topic_ssim: |                         |   3099/1464000 |   0%
	subject_11_topic_tesim: |                         |   3099/1464000 |   0%
subject_12_geographic_ssim: |                         |    205/1464000 |   0%
subject_12_geographic_tesim: |                         |    205/1464000 |   0%
	 subject_12_topic_ssim: |                         |   2572/1464000 |   0%
	subject_12_topic_tesim: |                         |   2572/1464000 |   0%
subject_13_geographic_ssim: |                         |     83/1464000 |   0%
subject_13_geographic_tesim: |                         |     83/1464000 |   0%
	 subject_13_topic_ssim: |                         |   1536/1464000 |   0%
	subject_13_topic_tesim: |                         |   1536/1464000 |   0%
subject_14_geographic_ssim: |                         |     29/1464000 |   0%
subject_14_geographic_tesim: |                         |     29/1464000 |   0%
	 subject_14_topic_ssim: |                         |   1536/1464000 |   0%
	subject_14_topic_tesim: |                         |   1536/1464000 |   0%
subject_15_geographic_ssim: |                         |     29/1464000 |   0%
subject_15_geographic_tesim: |                         |     29/1464000 |   0%
	 subject_15_topic_ssim: |                         |   1122/1464000 |   0%
	subject_15_topic_tesim: |                         |   1122/1464000 |   0%
subject_16_geographic_ssim: |                         |     29/1464000 |   0%
subject_16_geographic_tesim: |                         |     29/1464000 |   0%
	 subject_16_topic_ssim: |                         |     11/1464000 |   0%
	subject_16_topic_tesim: |                         |     11/1464000 |   0%
subject_17_geographic_ssim: |                         |     29/1464000 |   0%
subject_17_geographic_tesim: |                         |     29/1464000 |   0%
	 subject_17_topic_ssim: |                         |     11/1464000 |   0%
	subject_17_topic_tesim: |                         |     11/1464000 |   0%
subject_18_geographic_ssim: |                         |     29/1464000 |   0%
subject_18_geographic_tesim: |                         |     29/1464000 |   0%
	 subject_18_topic_ssim: |                         |     11/1464000 |   0%
	subject_18_topic_tesim: |                         |     11/1464000 |   0%
subject_19_geographic_ssim: |                         |     29/1464000 |   0%
subject_19_geographic_tesim: |                         |     29/1464000 |   0%
	 subject_19_topic_ssim: |                         |     11/1464000 |   0%
	subject_19_topic_tesim: |                         |     11/1464000 |   0%
subject_1_geographic_ssim: |==                       | 122528/1464000 |   8%
subject_1_geographic_tesim: |==                       | 122528/1464000 |   8%
subject_1_temporal_tesim: |                         |  11379/1464000 |   0%
		subject_1_topic_ssim: |==============           | 829384/1464000 |  56%
	 subject_1_topic_tesim: |==============           | 829384/1464000 |  56%
subject_20_geographic_ssim: |                         |     29/1464000 |   0%
subject_20_geographic_tesim: |                         |     29/1464000 |   0%
	 subject_20_topic_ssim: |                         |     11/1464000 |   0%
	subject_20_topic_tesim: |                         |     11/1464000 |   0%
subject_21_geographic_ssim: |                         |     29/1464000 |   0%
subject_21_geographic_tesim: |                         |     29/1464000 |   0%
	 subject_21_topic_ssim: |                         |     11/1464000 |   0%
	subject_21_topic_tesim: |                         |     11/1464000 |   0%
subject_22_geographic_ssim: |                         |     29/1464000 |   0%
subject_22_geographic_tesim: |                         |     29/1464000 |   0%
subject_23_geographic_ssim: |                         |     29/1464000 |   0%
subject_23_geographic_tesim: |                         |     29/1464000 |   0%
subject_24_geographic_ssim: |                         |     29/1464000 |   0%
subject_24_geographic_tesim: |                         |     29/1464000 |   0%
subject_25_geographic_ssim: |                         |     29/1464000 |   0%
subject_25_geographic_tesim: |                         |     29/1464000 |   0%
subject_26_geographic_ssim: |                         |     29/1464000 |   0%
subject_26_geographic_tesim: |                         |     29/1464000 |   0%
subject_27_temporal_tesim: |                         |     29/1464000 |   0%
	 subject_28_topic_ssim: |                         |     29/1464000 |   0%
	subject_28_topic_tesim: |                         |     29/1464000 |   0%
subject_2_geographic_ssim: |=                        | 100896/1464000 |   6%
subject_2_geographic_tesim: |=                        | 100896/1464000 |   6%
subject_2_temporal_tesim: |                         |   3607/1464000 |   0%
		subject_2_topic_ssim: |=======                  | 453270/1464000 |  30%
	 subject_2_topic_tesim: |=======                  | 453270/1464000 |  30%
subject_36_geographic_ssim: |                         |    633/1464000 |   0%
subject_36_geographic_tesim: |                         |    633/1464000 |   0%
	 subject_36_topic_ssim: |                         |    633/1464000 |   0%
	subject_36_topic_tesim: |                         |    633/1464000 |   0%
subject_3_geographic_ssim: |                         |  52154/1464000 |   3%
subject_3_geographic_tesim: |                         |  52154/1464000 |   3%
subject_3_temporal_tesim: |                         |   4195/1464000 |   0%
		subject_3_topic_ssim: |===                      | 212174/1464000 |  14%
	 subject_3_topic_tesim: |===                      | 212174/1464000 |  14%
subject_4_geographic_ssim: |                         |  20957/1464000 |   1%
subject_4_geographic_tesim: |                         |  20957/1464000 |   1%
subject_4_temporal_tesim: |                         |   2515/1464000 |   0%
		subject_4_topic_ssim: |==                       | 117491/1464000 |   8%
	 subject_4_topic_tesim: |==                       | 117491/1464000 |   8%
subject_5_geographic_ssim: |                         |   7920/1464000 |   0%
subject_5_geographic_tesim: |                         |   7920/1464000 |   0%
subject_5_temporal_tesim: |                         |    203/1464000 |   0%
		subject_5_topic_ssim: |=                        |  78380/1464000 |   5%
	 subject_5_topic_tesim: |=                        |  78380/1464000 |   5%
subject_6_geographic_ssim: |                         |   9647/1464000 |   0%
subject_6_geographic_tesim: |                         |   9647/1464000 |   0%
subject_6_temporal_tesim: |                         |    714/1464000 |   0%
		subject_6_topic_ssim: |                         |  27888/1464000 |   1%
	 subject_6_topic_tesim: |                         |  27888/1464000 |   1%
subject_7_geographic_ssim: |                         |   3160/1464000 |   0%
subject_7_geographic_tesim: |                         |   3160/1464000 |   0%
subject_7_temporal_tesim: |                         |     35/1464000 |   0%
		subject_7_topic_ssim: |                         |  16104/1464000 |   1%
	 subject_7_topic_tesim: |                         |  16104/1464000 |   1%
subject_8_geographic_ssim: |                         |    320/1464000 |   0%
subject_8_geographic_tesim: |                         |    320/1464000 |   0%
subject_8_temporal_tesim: |                         |    846/1464000 |   0%
		subject_8_topic_ssim: |                         |   9035/1464000 |   0%
	 subject_8_topic_tesim: |                         |   9035/1464000 |   0%
subject_9_geographic_ssim: |                         |    379/1464000 |   0%
subject_9_geographic_tesim: |                         |    379/1464000 |   0%
subject_9_temporal_tesim: |                         |     12/1464000 |   0%
		subject_9_topic_ssim: |                         |   8067/1464000 |   0%
	 subject_9_topic_tesim: |                         |   8067/1464000 |   0%
 subject_geographic_ssim: |======                   | 365049/1464000 |  24%
subject_geographic_tesim: |======                   | 365049/1464000 |  24%
	subject_temporal_tesim: |                         |  35039/1464000 |   2%
			subject_topic_ssim: |==================       | 1102483/1464000 |  75%
		 subject_topic_tesim: |==================       | 1102483/1464000 |  75%
				submitted_dttsim: |================         | 938954/1464000 |  64%
submitted_earliest_dttsi: |================         | 938954/1464000 |  64%
	submitted_latest_dttsi: |================         | 938954/1464000 |  64%
						sul_tag_ssim: |=========                | 540761/1464000 |  36%
supplement_resource_count_itsi: |                         |    344/1464000 |   0%
			sw_author_sort_ssi: |=========================| 1464000/1464000 | 100%
					sw_author_ssim: |===                      | 196587/1464000 |  13%
				 sw_author_tesim: |===                      | 196587/1464000 |  13%
	sw_display_title_tesim: |======================== | 1453308/1464000 |  99%
					sw_format_ssim: |=====================    | 1264124/1464000 |  86%
				 sw_format_tesim: |=========================| 1464000/1464000 | 100%
					 sw_genre_ssim: |                         |   3720/1464000 |   0%
					sw_genre_tesim: |=========================| 1464000/1464000 | 100%
				sw_language_ssim: |============             | 743147/1464000 |  50%
			 sw_language_tesim: |======================== | 1416605/1464000 |  96%
	 sw_pub_date_facet_ssi: |====================     | 1209830/1464000 |  82%
		sw_pub_date_sort_isi: |====================     | 1209830/1464000 |  82%
		sw_pub_date_sort_ssi: |====================     | 1209830/1464000 |  82%
sw_subject_geographic_ssim: |==========               | 625517/1464000 |  42%
sw_subject_geographic_tesim: |==========               | 625517/1464000 |  42%
sw_subject_temporal_ssim: |                         |  35039/1464000 |   2%
sw_subject_temporal_tesim: |                         |  35039/1464000 |   2%
					 sw_topic_ssim: |==================       | 1111488/1464000 |  75%
					sw_topic_tesim: |==================       | 1111488/1464000 |  75%
			system_create_dtsi: |=========================| 1464000/1464000 | 100%
		system_modified_dtsi: |=========================| 1464000/1464000 | 100%
								tag_ssim: |======================== | 1455523/1464000 |  99%
							 timestamp: |=========================| 1464000/1464000 | 100%
title_info_0_main_title_ssim: |=========================| 1464000/1464000 | 100%
title_info_10_main_title_ssim: |                         |   5094/1464000 |   0%
title_info_11_main_title_ssim: |                         |   5094/1464000 |   0%
title_info_12_main_title_ssim: |                         |    622/1464000 |   0%
title_info_13_main_title_ssim: |                         |    622/1464000 |   0%
title_info_14_main_title_ssim: |                         |    622/1464000 |   0%
title_info_15_main_title_ssim: |                         |    622/1464000 |   0%
title_info_1_main_title_ssim: |==                       | 142587/1464000 |   9%
title_info_2_main_title_ssim: |                         |  32021/1464000 |   2%
title_info_3_main_title_ssim: |                         |  21312/1464000 |   1%
title_info_4_main_title_ssim: |                         |  13471/1464000 |   0%
title_info_5_main_title_ssim: |                         |  12253/1464000 |   0%
title_info_6_main_title_ssim: |                         |   7235/1464000 |   0%
title_info_7_main_title_ssim: |                         |   5917/1464000 |   0%
title_info_8_main_title_ssim: |                         |   5304/1464000 |   0%
title_info_9_main_title_ssim: |                         |   5158/1464000 |   0%
title_info_main_title_ssim: |=========================| 1464000/1464000 | 100%
					title_sort_ssi: |======================== | 1463558/1464000 |  99%
							 title_ssi: |======================== | 1463414/1464000 |  99%
						 title_tesim: |======================== | 1463414/1464000 |  99%
							topic_ssim: |==================       | 1102483/1464000 |  75%
						 topic_tesim: |==================       | 1102483/1464000 |  75%
	twenty_pct_status_ssim: |======================== | 1455183/1464000 |  99%
twenty_pct_visibility_release_dtsim: |                         |   2095/1464000 |   0%
 use_license_machine_ssi: |===                      | 227806/1464000 |  15%
use_licenses_machine_ssim: |===                      | 227806/1464000 |  15%
use_licenses_machine_tesim: |===                      | 227806/1464000 |  15%
			use_statement_ssim: |====================     | 1206502/1464000 |  82%
						uuid_id_ssim: |======================== | 1453565/1464000 |  99%
						versions_ssm: |=========================| 1464000/1464000 | 100%
video_resource_count_itsi: |                         |   1662/1464000 |   0%
wf_accession2WF_sdr-ingest-transfer_dttsi: |                         |  13973/1464000 |   0%
wf_accessionWF_content-metadata_dttsi: |=============            | 799188/1464000 |  54%
wf_accessionWF_descriptive-metadata_dttsi: |=============            | 799188/1464000 |  54%
wf_accessionWF_end-accession_dttsi: |=============            | 799188/1464000 |  54%
wf_accessionWF_provenance-metadata_dttsi: |=============            | 799188/1464000 |  54%
wf_accessionWF_publish_dttsi: |=============            | 799188/1464000 |  54%
wf_accessionWF_remediate-object_dttsi: |=============            | 799188/1464000 |  54%
wf_accessionWF_reset-workspace_dttsi: |============             | 733064/1464000 |  50%
wf_accessionWF_rights-metadata_dttsi: |=============            | 799188/1464000 |  54%
wf_accessionWF_sdr-ingest-received_dttsi: |=============            | 799188/1464000 |  54%
wf_accessionWF_sdr-ingest-transfer_dttsi: |=============            | 799188/1464000 |  54%
wf_accessionWF_shelve_dttsi: |=============            | 799188/1464000 |  54%
wf_accessionWF_start-accession_dttsi: |=============            | 799188/1464000 |  54%
wf_accessionWF_technical-metadata_dttsi: |=============            | 799188/1464000 |  54%
wf_assemblyWF_accessioning-initiate_dttsi: |============             | 757639/1464000 |  51%
wf_assemblyWF_checksum-compute_dttsi: |============             | 757639/1464000 |  51%
wf_assemblyWF_exif-collect_dttsi: |============             | 757639/1464000 |  51%
wf_assemblyWF_jp2-create_dttsi: |============             | 749530/1464000 |  51%
wf_assemblyWF_start-assembly_dttsi: |============             | 757653/1464000 |  51%
wf_digitizationWF_digitize_dttsi: |                         |   7913/1464000 |   0%
wf_digitizationWF_initiate_dttsi: |=========                | 543603/1464000 |  37%
wf_digitizationWF_start-accession_dttsi: |                         |   7913/1464000 |   0%
wf_disseminationWF_cleanup_dttsi: |=============            | 799188/1464000 |  54%
wf_dpgImageWF_completeness_dttsi: |                         |   1066/1464000 |   0%
wf_dpgImageWF_copy_to_assembly_dttsi: |                         |  25311/1464000 |   1%
wf_dpgImageWF_delete_scratch_dttsi: |                         |  25923/1464000 |   1%
wf_dpgImageWF_digitized_dttsi: |                         |  25311/1464000 |   1%
wf_dpgImageWF_imageqc_dttsi: |                         |   1066/1464000 |   0%
wf_dpgImageWF_import_files_dttsi: |                         |  25311/1464000 |   1%
wf_dpgImageWF_initiate_dttsi: |                         |  53234/1464000 |   3%
wf_dpgImageWF_md5_gen_dttsi: |                         |  25311/1464000 |   1%
wf_dpgImageWF_md5_verify_assembly_dttsi: |                         |  25311/1464000 |   1%
wf_dpgImageWF_postprocessing_dttsi: |                         |   1066/1464000 |   0%
wf_dpgImageWF_scan_dttsi: |                         |   7980/1464000 |   0%
wf_dpgImageWF_tracking_db_dttsi: |                         |  53234/1464000 |   3%
wf_eemsAccessionWF_catalog-status_dttsi: |                         |   1149/1464000 |   0%
wf_eemsAccessionWF_check-marc_dttsi: |                         |   1149/1464000 |   0%
wf_eemsAccessionWF_eems-transfer_dttsi: |                         |   1149/1464000 |   0%
wf_eemsAccessionWF_other-metadata_dttsi: |                         |   1149/1464000 |   0%
wf_eemsAccessionWF_register-object_dttsi: |                         |   1149/1464000 |   0%
wf_eemsAccessionWF_start-accession_dttsi: |                         |     33/1464000 |   0%
wf_eemsAccessionWF_submit-marc_dttsi: |                         |   1149/1464000 |   0%
wf_eemsAccessionWF_submit-tech-services_dttsi: |                         |   1149/1464000 |   0%
					 wf_error_ssim: |                         |   1814/1464000 |   0%
wf_etdSubmitWF_binder-transfer_dttsi: |                         |   8448/1464000 |   0%
wf_etdSubmitWF_catalog-status_dttsi: |                         |  10679/1464000 |   0%
wf_etdSubmitWF_check-marc_dttsi: |                         |  10679/1464000 |   0%
wf_etdSubmitWF_other-metadata_dttsi: |                         |  10679/1464000 |   0%
wf_etdSubmitWF_reader-approval_dttsi: |                         |  10658/1464000 |   0%
wf_etdSubmitWF_register-object_dttsi: |                         |  10679/1464000 |   0%
wf_etdSubmitWF_registrar-approval_dttsi: |                         |  10679/1464000 |   0%
wf_etdSubmitWF_start-accession_dttsi: |                         |  10679/1464000 |   0%
wf_etdSubmitWF_submit-marc_dttsi: |                         |  10679/1464000 |   0%
wf_etdSubmitWF_submit_dttsi: |                         |  10679/1464000 |   0%
wf_gisAssemblyWF_assign-placenames_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_author-metadata_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_extract-boundingbox_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_extract-iso19139_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_extract-thumbnail_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_finish-data_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_finish-gis-assembly-workflow_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_finish-metadata_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_generate-content-metadata_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_generate-geo-metadata_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_generate-mods_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_load-geo-metadata_dttsi: |                         |   1664/1464000 |   0%
wf_gisAssemblyWF_normalize-data_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_package-data_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_register-druid_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_start-gis-assembly-workflow_dttsi: |                         |   1921/1464000 |   0%
wf_gisAssemblyWF_wrangle-data_dttsi: |                         |   1921/1464000 |   0%
wf_gisDeliveryWF_finish-gis-delivery-workflow_dttsi: |                         |   1921/1464000 |   0%
wf_gisDeliveryWF_load-geoserver_dttsi: |                         |   1921/1464000 |   0%
wf_gisDeliveryWF_load-raster_dttsi: |                         |   1921/1464000 |   0%
wf_gisDeliveryWF_load-vector_dttsi: |                         |   1921/1464000 |   0%
wf_gisDeliveryWF_start-gis-delivery-workflow_dttsi: |                         |   1921/1464000 |   0%
wf_gisDiscoveryWF_export-opengeometadata_dttsi: |                         |   1921/1464000 |   0%
wf_gisDiscoveryWF_finish-gis-discovery-workflow_dttsi: |                         |   1921/1464000 |   0%
wf_gisDiscoveryWF_generate-geoblacklight_dttsi: |                         |   1921/1464000 |   0%
wf_gisDiscoveryWF_load-geoblacklight_dttsi: |                         |   1921/1464000 |   0%
wf_gisDiscoveryWF_start-gis-discovery-workflow_dttsi: |                         |   1921/1464000 |   0%
wf_goobiWF_goobi-notify_dttsi: |                         |     27/1464000 |   0%
	wf_goobiWF_start_dttsi: |                         |     27/1464000 |   0%
wf_googleScannedBookWF_cleanup_dttsi: |==                       | 139800/1464000 |   9%
wf_googleScannedBookWF_descriptive-metadata_dttsi: |==                       | 140764/1464000 |   9%
wf_googleScannedBookWF_google-convert_dttsi: |==                       | 140736/1464000 |   9%
wf_googleScannedBookWF_google-download_dttsi: |==                       | 140736/1464000 |   9%
wf_googleScannedBookWF_process-content_dttsi: |==                       | 139869/1464000 |   9%
wf_googleScannedBookWF_register-object_dttsi: |==                       | 140773/1464000 |   9%
wf_googleScannedBookWF_sdr-ingest-deposit_dttsi: |==                       | 125428/1464000 |   8%
wf_googleScannedBookWF_sdr-ingest-transfer_dttsi: |==                       | 139834/1464000 |   9%
wf_googleScannedBookWF_shelve_dttsi: |==                       | 139869/1464000 |   9%
wf_hydrusAssemblyWF_approve_dttsi: |                         |   8123/1464000 |   0%
wf_hydrusAssemblyWF_start-assembly_dttsi: |                         |   8123/1464000 |   0%
wf_hydrusAssemblyWF_start-deposit_dttsi: |                         |   8603/1464000 |   0%
wf_hydrusAssemblyWF_submit_dttsi: |                         |   8123/1464000 |   0%
wf_registrationWF_register_dttsi: |==                       | 157176/1464000 |  10%
wf_releaseWF_release-members_dttsi: |==                       | 162772/1464000 |  11%
wf_releaseWF_release-publish_dttsi: |===                      | 177747/1464000 |  12%
wf_releaseWF_start_dttsi: |===                      | 177747/1464000 |  12%
wf_releaseWF_update-marc_dttsi: |===                      | 177747/1464000 |  12%
wf_sdrAuditWF_audit-verify_dttsi: |=                        |  66940/1464000 |   4%
wf_sdrIngestWF_complete-deposit_dttsi: |================         | 939022/1464000 |  64%
wf_sdrIngestWF_ingest-cleanup_dttsi: |=============            | 795461/1464000 |  54%
wf_sdrIngestWF_register-sdr_dttsi: |================         | 939022/1464000 |  64%
wf_sdrIngestWF_start-ingest_dttsi: |=============            | 813560/1464000 |  55%
wf_sdrIngestWF_transfer-object_dttsi: |================         | 939022/1464000 |  64%
wf_sdrIngestWF_validate-bag_dttsi: |================         | 939022/1464000 |  64%
wf_sdrIngestWF_verify-agreement_dttsi: |================         | 939022/1464000 |  64%
wf_sdrMigrationWF_migration-complete_dttsi: |                         |   2365/1464000 |   0%
wf_sdrMigrationWF_migration-metadata_dttsi: |                         |   2365/1464000 |   0%
wf_sdrMigrationWF_migration-register_dttsi: |                         |   2365/1464000 |   0%
wf_sdrMigrationWF_migration-start_dttsi: |                         |   2365/1464000 |   0%
wf_sdrMigrationWF_migration-transfer_dttsi: |                         |   2365/1464000 |   0%
								 wf_ssim: |======================== | 1454714/1464000 |  99%
wf_swIndexWF_indexed_to_localhost_dttsi: |                         |   2015/1464000 |   0%
wf_swIndexWF_indexed_to_sw-solr-test_dttsi: |                         |   2257/1464000 |   0%
						 wf_swp_ssim: |======================== | 1454714/1464000 |  99%
wf_versioningWF_start-accession_dttsi: |========                 | 490705/1464000 |  33%
wf_versioningWF_start-version_dttsi: |========                 | 494858/1464000 |  33%
wf_versioningWF_submit-version_dttsi: |========                 | 490705/1464000 |  33%
wf_wasCrawlDisseminationWF_cdx-generator_dttsi: |                         |  19476/1464000 |   1%
wf_wasCrawlDisseminationWF_cdx-merge-sort-publish_dttsi: |                         |  18863/1464000 |   1%
wf_wasCrawlDisseminationWF_path-indexer_dttsi: |                         |  18571/1464000 |   1%
wf_wasCrawlDisseminationWF_start_dttsi: |                         |  19476/1464000 |   1%
wf_wasCrawlPreassemblyWF_build-was-crawl-druid-tree_dttsi: |                         |  18842/1464000 |   1%
wf_wasCrawlPreassemblyWF_content-metadata-generator_dttsi: |                         |  18842/1464000 |   1%
wf_wasCrawlPreassemblyWF_desc-metadata-generator_dttsi: |                         |  18842/1464000 |   1%
wf_wasCrawlPreassemblyWF_end-was-crawl-preassembly_dttsi: |                         |  18842/1464000 |   1%
wf_wasCrawlPreassemblyWF_metadata-extractor_dttsi: |                         |  18842/1464000 |   1%
wf_wasCrawlPreassemblyWF_start_dttsi: |                         |  18842/1464000 |   1%
wf_wasCrawlPreassemblyWF_technical-metadata-generator_dttsi: |                         |  18842/1464000 |   1%
wf_wasDisseminationWF_start-special-dissemination_dttsi: |                         |  18858/1464000 |   1%
wf_wasDisseminationWF_start_dttsi: |                         |  18858/1464000 |   1%
						 wf_wps_ssim: |======================== | 1454714/1464000 |  99%
						 wf_wsp_ssim: |======================== | 1454714/1464000 |  99%
		workflow_status_ssim: |======================== | 1454714/1464000 |  99%
```

## PURL (status == "published")

PURLs taken from Purl Fetcher REST Endpoint. Total number of PURL objects: between 962900 and 963000 objects. Metadata harvested from dereferencing PURL.

PURL: https://purl-fetcher-prod.stanford.edu/purls

### Fields




## Fedora 3 (dor-prod)

### Streams

- DC: Dublin Core Record for this object	text/xml
- RELS-EXT: Fedora Object-to-Object Relationship Metadata	application/rdf+xml
- identityMetadata: Identity Metadata	text/xml
- workflows: Workflow	application/xml
- descMetadata: Descriptive Metadata	text/xml
- rightsMetadata: Rights Metadata	text/xml
- contentMetadata: Content Metadata	text/xml
- technicalMetadata: Technical Metadata	text/xml
- provenanceMetadata: Provenance Metadata	text/xml
- versionMetadata: Version Metadata	text/xml
- events: Events	text/xml

## System stats



## DRUIDs (SURI)

All DRUIDs (identifiers minted in SURI within the DRUID namespace):

```
/identifier/created: |=========================| 1534100/1534100 | 100%
/identifier/createdBy: |=========================| 1534100/1534100 | 100%
     /identifier/id: |=========================| 1534100/1534100 | 100%
```

Unique fields and number of results for each field in "/identifier/createdBy":

```
187792 'dor'
103814 'hydra-etd'
1209606 'labware'
32888 'xforms'
```


## Stacks

Filesystem (‘shelves’): /home/lyberadmin/stacks/
	number of files:



## Preservation Core
