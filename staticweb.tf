#########################################################
####Create the Storage bucket in the US multi-region#####
#########################################################

#resource "random_id" "bucket_prefix" {
#  byte_length = 8
#}

resource "google_storage_bucket" "mbrandmcloudresume" {
  name          = "mbrandmcloudresume01.com"
  location      = "US"
  storage_class = "NEARLINE"

  uniform_bucket_level_access = false
  
  website {
    main_page_suffix = "index.html"
    not_found_page   = "404.html"
  }
  cors {
    origin          = ["http://mbrandmcloudresume.com"]
    method          = ["GET","POST"]
    response_header = ["*"]
    max_age_seconds = 3600
  }
}
#########################################################
####Upload index.html to mbrandmcloudresume.com bucket###
#########################################################
# Upload a simple index.html page to the bucket
resource "google_storage_bucket_object" "indexpage" {
  name         = "index.html"
  source      = "index.html"
  bucket       = google_storage_bucket.mbrandmcloudresume.id

}
# Upload a simple 404 / error page to the bucket
resource "google_storage_bucket_object" "errorpage" {
  name         = "404.html"
  source      = "404.html"
  content_type = "text/html"
  bucket       = google_storage_bucket.mbrandmcloudresume.id
}

#########################################################
##########Make the files public to the internet##########
#########################################################
##  

resource "google_storage_bucket_access_control" "public_rule" {
  bucket = google_storage_bucket.mbrandmcloudresume.id
  role   = "READER"
  entity = "allUsers"
}
