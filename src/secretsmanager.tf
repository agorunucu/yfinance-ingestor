# Secrets should be stored in the Secrets Manager.
# But the current permissions does not permit to retrieve secret data.
# So, these resources are not used at the moment.
# I will not delete them for the possible future improvements.
resource "google_secret_manager_secret" "snowflake_account" {
  secret_id = "snowflake_account"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret" "snowflake_user" {
  secret_id = "snowflake_user"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret" "snowflake_password" {
  secret_id = "snowflake_password"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret" "snowflake_database" {
  secret_id = "snowflake_database"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret" "snowflake_schema" {
  secret_id = "snowflake_schema"
  replication {
    automatic = true
  }
}
