output "instance_pub_ip" {
  value = aws_instance.sqs-testing.public_ip
}