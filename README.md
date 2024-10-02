# Monitoring-Scaling-and-Automation

output
S3 Bucket mandarpdevops created successfully.
File /home/mandar/DevOps/Monitoring-Scaling-and-Automation/HTML/index.html uploaded to S3 bucket mandarpdevops as index.html.
Load Balancer created with ARN: arn:aws:elasticloadbalancing:us-west-2:975050024946:loadbalancer/app/mp-webapp-lb/b0aa369c2ac603ee
Waiting for Load Balancer arn:aws:elasticloadbalancing:us-west-2:975050024946:loadbalancer/app/mp-webapp-lb/b0aa369c2ac603ee to be active...
Load Balancer arn:aws:elasticloadbalancing:us-west-2:975050024946:loadbalancer/app/mp-webapp-lb/b0aa369c2ac603ee is now active.
Target group created with ARN: arn:aws:elasticloadbalancing:us-west-2:975050024946:targetgroup/mp-webapp-target-group/d355b06ba07687c2
Listener created for Load Balancer.
Launch Configuration mp-webapp-launch-config created.
Auto Scaling Group created and registered with Target Group.
Scaling policy for scaling up created.
Waiting for instances in Auto Scaling Group mp-webapp-asg to be 'running'...
All instances in Auto Scaling Group mp-webapp-asg are now 'running'.
SNS Topic created with ARN: arn:aws:sns:us-west-2:975050024946:mp-webapp-notifications
Subscription created for mandarphadke1434@gmail.com. Please check your email to confirm the subscription.
CloudWatch alarm created to monitor unhealthy instances.