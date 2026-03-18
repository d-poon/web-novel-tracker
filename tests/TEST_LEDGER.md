_This file is auto-generated. Do not edit manually._

# AI vs Human Test Ledger

**Project:** Novel Tracker
**Maintainer:** Dennis Poon
**Date:** 2026-03-18

## Test Matrix

| Name                                               | Module             | Type | AI? | NonAI? | Reviewed? | Notes |
| -------------------------------------------------- | ------------------ | ---- | --- | ------ | --------- | -----|
| test_get_connection_returns_valid_connection       | test_database.py   | test | ✅   |        | ✅         |       |
| test_connection_has_row_factory                    | test_database.py   | test | ✅   |        | ✅         |       |
| test_database_file_exists_after_connection         | test_database.py   | test | ✅   |        | ✅         |       |
| test_initialize_db_creates_table                   | test_database.py   | test | ✅   |        | ✅         |       |
| test_novels_table_has_correct_columns              | test_database.py   | test | ✅   |        | ✅         |       |
| test_id_column_is_primary_key_autoincrement        | test_database.py   | test | ✅   |        | ✅         |       |
| test_initialize_db_idempotent                      | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_insert                          | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_fetch_one                       | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_fetch_all                       | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_with_mapper                     | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_with_mapper_fetch_all           | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_parameterized_prevents_injec... | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_no_params                       | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_fetch_none_when_no_results      | test_database.py   | test | ✅   |        | ✅         |       |
| test_execute_query_fetch_empty_list_when_no_res... | test_database.py   | test | ✅   |        | ✅         |       |
| test_insert_duplicate_unique_constraint            | test_database.py   | test | ✅   |        | ✅         |       |
| test_insert_missing_required_field                 | test_database.py   | test | ✅   |        | ✅         |       |
| test_query_with_invalid_table                      | test_database.py   | test | ✅   |        | ✅         |       |
| test_query_with_type_mismatch_in_insert            | test_database.py   | test | ✅   |        | ✅         |       |
| test_data_persists_after_connection_close          | test_database.py   | test | ✅   |        | ✅         |       |
| test_multiple_inserts_accumulate                   | test_database.py   | test | ✅   |        | ✅         |       |
| test_updates_persist                               | test_database.py   | test | ✅   |        | ✅         |       |
| test_delete_persists                               | test_database.py   | test | ✅   |        | ✅         |       |
| test_add_novel_minimal                             | test_repository.py | test | ✅   |        | ✅         |       |
| test_add_novel_complete                            | test_repository.py | test | ✅   |        | ✅         |       |
| test_add_multiple_novels                           | test_repository.py | test | ✅   |        | ✅         |       |
| test_list_novels_empty_database                    | test_repository.py | test | ✅   |        | ✅         |       |
| test_list_novels_returns_all                       | test_repository.py | test | ✅   |        | ✅         |       |
| test_list_novels_preserves_data                    | test_repository.py | test | ✅   |        | ✅         |       |
| test_get_novel_by_title_exists                     | test_repository.py | test | ✅   |        | ✅         |       |
| test_get_novel_by_title_not_exists                 | test_repository.py | test | ✅   |        | ✅         |       |
| test_get_novel_by_title_case_sensitive             | test_repository.py | test | ✅   | ✅      | ✅         |       |
| test_update_novel_single_field                     | test_repository.py | test | ✅   |        | ✅         |       |
| test_update_novel_multiple_fields                  | test_repository.py | test | ✅   |        | ✅         |       |
| test_update_novel_preserves_other_fields           | test_repository.py | test | ✅   |        | ✅         |       |
| test_update_nonexistent_novel                      | test_repository.py | test | ✅   |        | ✅         |       |
| test_delete_novel_exists                           | test_repository.py | test | ✅   |        | ✅         |       |
| test_delete_novel_not_exists                       | test_repository.py | test | ✅   |        | ✅         |       |
| test_delete_removes_only_target_novel              | test_repository.py | test | ✅   |        | ✅         |       |
| test_novel_with_special_characters_in_title        | test_repository.py | test | ✅   |        | ✅         |       |
| test_novel_with_unicode_characters                 | test_repository.py | test | ✅   |        | ✅         |       |
| test_total_novels_empty_database                   | test_repository.py | test | ✅   |        | ✅         |       |
| test_total_novels_with_data                        | test_repository.py | test | ✅   |        | ✅         |       |
| test_total_chapters_read_empty_database            | test_repository.py | test | ✅   |        | ✅         |       |
| test_total_chapters_read_with_data                 | test_repository.py | test | ✅   |        | ✅         |       |
| test_average_chapters_per_novel_empty_database     | test_repository.py | test | ✅   |        | ✅         |       |
| test_average_chapters_per_novel_with_data          | test_repository.py | test | ✅   |        | ✅         |       |
| test_most_recently_read_empty_database             | test_repository.py | test | ✅   |        | ✅         |       |
| test_most_recently_read_with_data                  | test_repository.py | test | ✅   |        | ✅         |       |
| test_most_used_sites_empty_database                | test_repository.py | test | ✅   |        | ✅         |       |
| test_most_used_sites_with_data                     | test_repository.py | test | ✅   |        | ✅         |       |
| test_novels_by_site_exists                         | test_repository.py | test | ✅   |        | ✅         |       |
| test_novels_by_site_not_exists                     | test_repository.py | test | ✅   |        | ✅         |       |
| test_novels_by_site_case_insensitive               | test_repository.py | test | ✅   |        | ✅         |       |
| test_count_novels_by_site_exists                   | test_repository.py | test | ✅   |        | ✅         |       |
| test_count_novels_by_site_not_exists               | test_repository.py | test | ✅   |        | ✅         |       |
| test_recently_read_novels_default_period           | test_repository.py | test | ✅   |        | ✅         |       |
| test_recently_read_novels_custom_period            | test_repository.py | test | ✅   |        | ✅         |       |
| test_recently_updated_novels_default_limit         | test_repository.py | test | ✅   |        | ✅         |       |
| test_recently_updated_novels_custom_limit          | test_repository.py | test | ✅   |        | ✅         |       |
| test_longest_novels_read_default_limit             | test_repository.py | test | ✅   |        | ✅         |       |
| test_longest_novels_read_custom_limit              | test_repository.py | test | ✅   |        | ✅         |       |
| test_longest_novels_read_ordering                  | test_repository.py | test | ✅   |        | ✅         |       |
| test_read_after_write_consistency                  | test_repository.py | test | ✅   |        | ✅         |       |
| test_update_then_read_consistency                  | test_repository.py | test | ✅   |        | ✅         |       |
| test_delete_then_list_consistency                  | test_repository.py | test | ✅   |        | ✅         |       |
| test_stats_accuracy_after_operations               | test_repository.py | test | ✅   |        | ✅         |       |
| test_build_novel_minimal_input                     | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_complete_input                    | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_whitespace_handling               | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_edge_cases                        | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_url_conversion                    | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_date_preservation                 | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_none_handling                     | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_type_coercion                     | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_field_mapping                     | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_creates_new_instance              | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_sort_by_input_returns_enum              | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_sort_by_input_all_fields                | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_sort_by_input_string_conversion         | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_with_validated_schema             | test_builders.py   | test | ✅   |        | ✅         |       |
| test_builders_handle_validation_errors_upstream    | test_builders.py   | test | ✅   |        | ✅         |       |
| test_builder_chain_with_sort_field                 | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_novel_none_input                        | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_sort_by_input_none                      | test_builders.py   | test | ✅   |        | ✅         |       |
| test_build_sort_by_input_invalid_type              | test_builders.py   | test | ✅   |        | ✅         |       |
| test_title_blank_raises_value_error                | test_models.py     | test | ✅   |        | ✅         |       |
| test_missing_title_raises_validation_error         | test_models.py     | test | ✅   |        | ✅         |       |
| test_title_is_stripped_and_accepts_unicode_and_... | test_models.py     | test | ✅   |        | ✅         |       |
| test_site_trimming_and_empty_handling              | test_models.py     | test | ✅   |        | ✅         |       |
| test_url_accepts_valid_and_rejects_invalid         | test_models.py     | test | ✅   |        | ✅         |       |
| test_current_chapter_validation_behaviour          | test_models.py     | test | ✅   |        | ✅         |       |
| test_last_read_date_parsing_and_validation         | test_models.py     | test | ✅   |        | ✅         |       |
| test_notes_optional_preserved_and_none             | test_models.py     | test | ✅   |        | ✅         |       |
| test_novel_dataclass_and_row_to_novel              | test_models.py     | test | ✅   |        | ✅         |       |
| test_row_to_novel_missing_key_raises               | test_models.py     | test | ✅   |        | ✅         |       |
| test_row_to_novel_non_iso_date_raises_value_error  | test_models.py     | test | ✅   |        | ✅         |       |
| test_row_to_novel_numeric_chapter_as_string_is_... | test_models.py     | test | ✅   |        | ✅         |       |
| test_url_edge_cases_and_scheme_rejection           | test_models.py     | test | ✅   |        | ✅         |       |
| test_current_chapter_extremely_large               | test_models.py     | test | ✅   |        | ✅         |       |
| test_last_read_date_leap_and_future_dates          | test_models.py     | test | ✅   |        | ✅         |       |
| test_notes_preserve_large_content                  | test_models.py     | test | ✅   |        | ✅         |       |
| test_valid_titles                                  | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_title_stripping                               | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_title_with_special_characters                 | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_title_unicode_support                         | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_title_very_long                               | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_site_validation_cases                         | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_site_special_characters                       | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_site_unicode                                  | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_valid_urls                                    | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_invalid_urls                                  | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_url_none                                      | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_url_with_fragment_and_query                   | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_valid_current_chapter_values                  | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_current_chapter_none_defaults_to_zero         | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_invalid_current_chapter_values                | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_invalid_current_chapter_types                 | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_current_chapter_large_values                  | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_current_chapter_zero_explicit                 | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_valid_date_objects                            | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_date_none                                     | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_date_today                                    | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_date_future                                   | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_date_past                                     | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_none                                    | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_empty_string                            | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_normal_string                           | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_multiline                               | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_special_characters                      | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_unicode                                 | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_notes_very_long                               | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_all_enum_values_accessible                    | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_enum_string_values                            | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_enum_membership                               | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_enum_iteration                                | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_minimal_valid_creation                        | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_complete_valid_creation                       | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_whitespace_handling                           | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_edge_cases                                    | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_model_dump                                    | test_schemas.py    | test | ✅   |        | ✅         |       |
| test_json_serialization                            | test_schemas.py    | test | ✅   |        | ✅         |       |
## Fixture Matrix

| Name | Module | Type | AI? | NonAI? | Reviewed? | Notes |
| ---- | ------ | ---- | --- | ------ | --------- | -----|