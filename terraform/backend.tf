terraform {
  backend "s3" {
    bucket  = "luizscofield-terraform-states"
    region  = "us-east-1"
    key     = "sns-state"
    profile = "personal"
  }
}
