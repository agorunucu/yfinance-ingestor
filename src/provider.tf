terraform {
  backend "gcs" {
    bucket  = "bux-bi-assignment-agorunucu"
    prefix  = "tfstate"
  }
}

provider "google" {
  project     = "bux-bi-assignment-agorunucu"
  region      = "europe-west4"
}
