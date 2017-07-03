provider "aws" {}

resource "aws_instance" "example" {
  ami           = "ami-7a85a01a"
  instance_type = "t2.micro"
}