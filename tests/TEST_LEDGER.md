_This file is auto-generated. Do not edit manually._

# AI vs Human Test Ledger

**Project:** Novel Tracker
**Maintainer:** Dennis Poon
**Date:** 2026-03-18

## Test Matrix

| Name                                | Module             | Type | AI? | NonAI? | Reviewed? | Notes |
| ----------------------------------- | ------------------ | ---- | --- | ------ | --------- | ----- |
| test_get_connection_returns_vali... | test_database.py   | test | ✅   |        | ✅         |       |
| test_connection_has_row_factory     | test_database.py   | test | ✅   |        | ✅         |       |
| test_database_file_exists_after_... | test_database.py   | test | ✅   |        | ✅         |       |
| test_initialize_db_creates_table    | test_database.py   | test | ✅   |        | ✅         |       |
| test_novels_table_has_correct_co... | test_database.py   | test | ✅   |        | ✅         |       |
| test_id_column_is_primary_key_au... | test_database.py   | test | ✅   |        | ✅         |       |
| test_initialize_db_idempotent       | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_insert           | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_fetch_one        | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_fetch_all        | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_with_mapper      | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_with_mapper_f... | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_parameterized... | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_no_params        | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_fetch_none_wh... | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_fetch_empty_l... | test_database.py   | test | ✅   |        | ✅         |       |
| test_insert_duplicate_unique_con... | test_database.py   | test | ✅   |        | ✅         |       |
| test_insert_missing_required_field  | test_database.py   | test | ✅   |        | ✅         |       |
| test_query_with_invalid_table       | test_database.py   | test | ✅   |        | ✅         |       |
| test_query_with_type_mismatch_in... | test_database.py   | test | ✅   |        | ✅         |       |
| test_data_persists_after_connect... | test_database.py   | test | ✅   |        | ✅         |       |
| test_multiple_inserts_accumulate    | test_database.py   | test | ✅   |        | ✅         |       |
| test_updates_persist                | test_database.py   | test | ✅   |        | ✅         |       |
| test_delete_persists                | test_database.py   | test | ✅   |        | ✅         |       |
| test_add_novel_minimal              | test_repository.py | test | ✅   |        | ✅         |       |
| test_add_novel_complete             | test_repository.py | test | ✅   |        | ✅         |       |
| test_add_multiple_novels            | test_repository.py | test | ✅   |        | ✅         |       |
| test_list_novels_empty_database     | test_repository.py | test | ✅   |        | ✅         |       |
| test_list_novels_returns_all        | test_repository.py | test | ✅   |        | ✅         |       |
| test_list_novels_preserves_data     | test_repository.py | test | ✅   |        | ✅         |       |
| test_get_novel_by_title_exists      | test_repository.py | test | ✅   |        | ✅         |       |
| test_get_novel_by_title_not_exists  | test_repository.py | test | ✅   |        | ✅         |       |
| test_get_novel_by_title_case_sen... | test_repository.py | test | ✅   | ✅      | ✅         |       |
| test_update_novel_single_field      | test_repository.py | test | ✅   |        | ✅         |       |
| test_update_novel_multiple_fields   | test_repository.py | test | ✅   |        | ✅         |       |
| test_update_novel_preserves_othe... | test_repository.py | test | ✅   |        | ✅         |       |
| test_update_nonexistent_novel       | test_repository.py | test | ✅   |        | ✅         |       |
| test_delete_novel_exists            | test_repository.py | test | ✅   |        | ✅         |       |
| test_delete_novel_not_exists        | test_repository.py | test | ✅   |        | ✅         |       |
| test_delete_removes_only_target_... | test_repository.py | test | ✅   |        | ✅         |       |
| test_novel_with_special_characte... | test_repository.py | test | ✅   |        | ✅         |       |
| test_novel_with_unicode_characters  | test_repository.py | test | ✅   |        | ✅         |       |
| test_total_novels_empty_database    | test_repository.py | test | ✅   |        | ✅         |       |
| test_total_novels_with_data         | test_repository.py | test | ✅   |        | ✅         |       |
| test_total_chapters_read_empty_d... | test_repository.py | test | ✅   |        | ✅         |       |
| test_total_chapters_read_with_data  | test_repository.py | test | ✅   |        | ✅         |       |
| test_average_chapters_per_novel_... | test_repository.py | test | ✅   |        | ✅         |       |
| test_average_chapters_per_novel_... | test_repository.py | test | ✅   |        | ✅         |       |
| test_most_recently_read_empty_da... | test_repository.py | test | ✅   |        | ✅         |       |
| test_most_recently_read_with_data   | test_repository.py | test | ✅   |        | ✅         |       |
| test_most_used_sites_empty_database | test_repository.py | test | ✅   |        | ✅         |       |
| test_most_used_sites_with_data      | test_repository.py | test | ✅   |        | ✅         |       |
| test_novels_by_site_exists          | test_repository.py | test | ✅   |        | ✅         |       |
| test_novels_by_site_not_exists      | test_repository.py | test | ✅   |        | ✅         |       |
| test_novels_by_site_case_insensi... | test_repository.py | test | ✅   |        | ✅         |       |
| test_count_novels_by_site_exists    | test_repository.py | test | ✅   |        | ✅         |       |
| test_count_novels_by_site_not_ex... | test_repository.py | test | ✅   |        | ✅         |       |
| test_recently_read_novels_defaul... | test_repository.py | test | ✅   |        | ✅         |       |
| test_recently_read_novels_custom... | test_repository.py | test | ✅   |        | ✅         |       |
| test_recently_updated_novels_def... | test_repository.py | test | ✅   |        | ✅         |       |
| test_recently_updated_novels_cus... | test_repository.py | test | ✅   |        | ✅         |       |
| test_longest_novels_read_default... | test_repository.py | test | ✅   |        | ✅         |       |
| test_longest_novels_read_custom_... | test_repository.py | test | ✅   |        | ✅         |       |
| test_longest_novels_read_ordering   | test_repository.py | test | ✅   |        | ✅         |       |
| test_read_after_write_consistency   | test_repository.py | test | ✅   |        | ✅         |       |
| test_update_then_read_consistency   | test_repository.py | test | ✅   |        | ✅         |       |
| test_delete_then_list_consistency   | test_repository.py | test | ✅   |        | ✅         |       |
| test_stats_accuracy_after_operat... | test_repository.py | test | ✅   |        | ✅         |       |
| test_build_novel_minimal_input      | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_complete_input     | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_whitespace_hand... | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_edge_cases         | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_url_conversion     | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_date_preservation  | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_none_handling      | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_type_coercion      | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_field_mapping      | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_creates_new_ins... | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_sort_by_input_returns... | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_sort_by_input_all_fields | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_sort_by_input_string_... | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_with_validated_... | test_builders.py   | test | ✅   |        | ✅         |       |
| test_builders_handle_validation_... | test_builders.py   | test | ✅   |        | ✅         |       |
| test_builder_chain_with_sort_field  | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_none_input         | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_sort_by_input_none       | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_sort_by_input_invalid... | test_builders.py   | test | ✅   |        | ✅         |       |
| test_title_blank_raises_value_error | test_models.py     | test | ✅   |        | ✅         |       |
| test_missing_title_raises_valida... | test_models.py     | test | ✅   |        | ✅         |       |
| test_title_is_stripped_and_accep... | test_models.py     | test | ✅   |        | ✅         |       |
| test_site_trimming_and_empty_han... | test_models.py     | test | ✅   |        | ✅         |       |
| test_url_accepts_valid_and_rejec... | test_models.py     | test | ✅   |        | ✅         |       |
| test_current_chapter_validation_... | test_models.py     | test | ✅   |        | ✅         |       |
| test_last_read_date_parsing_and_... | test_models.py     | test | ✅   |        | ✅         |       |
| test_notes_optional_preserved_an... | test_models.py     | test | ✅   |        | ✅         |       |
| test_novel_dataclass_and_row_to_... | test_models.py     | test | ✅   |        | ✅         |       |
| test_row_to_novel_missing_key_ra... | test_models.py     | test | ✅   |        | ✅         |       |
| test_row_to_novel_non_iso_date_r... | test_models.py     | test | ✅   |        | ✅         |       |
| test_row_to_novel_numeric_chapte... | test_models.py     | test | ✅   |        | ✅         |       |
| test_url_edge_cases_and_scheme_r... | test_models.py     | test | ✅   |        | ✅         |       |
| test_current_chapter_extremely_l... | test_models.py     | test | ✅   |        | ✅         |       |
| test_last_read_date_leap_and_fut... | test_models.py     | test | ✅   |        | ✅         |       |
| test_notes_preserve_large_content   | test_models.py     | test | ✅   |        | ✅         |       |
| test_valid_titles                   | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_title_stripping                | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_title_with_special_characters  | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_title_unicode_support          | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_title_very_long                | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_site_validation_cases          | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_site_special_characters        | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_site_unicode                   | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_valid_urls                     | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_invalid_urls                   | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_url_none                       | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_url_with_fragment_and_query    | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_valid_current_chapter_values   | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_current_chapter_none_defaul... | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_invalid_current_chapter_values | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_invalid_current_chapter_types  | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_current_chapter_large_values   | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_current_chapter_zero_explicit  | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_valid_date_objects             | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_date_none                      | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_date_today                     | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_date_future                    | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_date_past                      | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_none                     | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_empty_string             | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_normal_string            | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_multiline                | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_special_characters       | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_unicode                  | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_very_long                | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_all_enum_values_accessible     | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_enum_string_values             | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_enum_membership                | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_enum_iteration                 | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_minimal_valid_creation         | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_complete_valid_creation        | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_whitespace_handling            | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_edge_cases                     | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_model_dump                     | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_json_serialization             | test_schemas.py    | test | ✅   |        | ✅         |       |

## Fixture Matrix

| Name                                | Module          | Type    | AI? | NonAI? | Reviewed? | Notes                                                        |
| ----------------------------------- | --------------- | ------- | --- | ------ | --------- | ------------------------------------------------------------ |
| temp_db                             | sample_database | fixture | ✅   |        | ✅         | Fixture that provides an isolated temporary SQLite databa... |
| db_connection                       | sample_database | fixture | ✅   |        | ✅         | Fixture that provides a connection to the temporary test ... |
| empty_db                            | sample_database | fixture | ✅   |        | ✅         | Fixture that provides an empty initialized test database.... |
| db_with_sample_novels               | sample_database | fixture | ✅   |        | ✅         | Fixture that provides a test database pre-populated with ... |
| novel_repository                    | sample_database | fixture | ✅   |        | ✅         | Fixture that provides a NovelRepository instance connecte... |
| minimal_novel_create                | sample_novels   | fixture | ✅   |        | ✅         | Minimal valid NovelCreate with only required title field.    |
| complete_novel_create               | sample_novels   | fixture | ✅   |        | ✅         | Complete NovelCreate with all fields populated.              |
| novel_create_with_whitespace        | sample_novels   | fixture | ✅   |        | ✅         | NovelCreate with leading/trailing whitespace that should ... |
| novel_create_with_edge_cases        | sample_novels   | fixture | ✅   |        | ✅         | NovelCreate with edge case values.                           |
| invalid_novel_data_empty_title      | sample_novels   | fixture | ✅   |        | ✅         | Data that should fail validation due to empty title.         |
| invalid_novel_data_whitespace_title | sample_novels   | fixture | ✅   |        | ✅         | Data that should fail validation due to whitespace-only t... |
| invalid_novel_data_negative_chapter | sample_novels   | fixture | ✅   |        | ✅         | Data that should fail validation due to negative chapter.    |
| invalid_novel_data_wrong_chapter... | sample_novels   | fixture | ✅   |        | ✅         | Data that should fail validation due to wrong chapter type.  |
| invalid_novel_data_invalid_url      | sample_novels   | fixture | ✅   |        | ✅         | Data that should fail validation due to invalid URL.         |
| all_sort_fields                     | sample_novels   | fixture | ✅   |        | ✅         | All valid NovelSortField enum values.                        |
| expected_minimal_novel_dict         | sample_novels   | fixture | ✅   |        | ✅         | Expected dictionary representation of minimal novel.         |
| expected_complete_novel_dict        | sample_novels   | fixture | ✅   |        | ✅         | Expected dictionary representation of complete novel.        |
| expected_whitespace_stripped_nov... | sample_novels   | fixture | ✅   |        | ✅         | Expected dictionary after whitespace stripping.              |
| title_validation_case               | sample_novels   | fixture | ✅   |        | ✅         | Parameterized fixture for title validation test cases.       |
| site_validation_case                | sample_novels   | fixture | ✅   |        | ✅         | Parameterized fixture for site validation test cases.        |
| valid_current_chapter_case          | sample_novels   | fixture | ✅   |        | ✅         | Parameterized fixture for valid current_chapter values.      |
| invalid_current_chapter_case        | sample_novels   | fixture | ✅   |        | ✅         | Parameterized fixture for invalid current_chapter values.    |
| invalid_current_chapter_type_case   | sample_novels   | fixture | ✅   |        | ✅         | Parameterized fixture for invalid current_chapter types.     |
| valid_url_case                      | sample_novels   | fixture | ✅   |        | ✅         | Parameterized fixture for valid URL test cases.              |
| invalid_url_case                    | sample_novels   | fixture | ✅   |        | ✅         | Parameterized fixture for invalid URL test cases.            |