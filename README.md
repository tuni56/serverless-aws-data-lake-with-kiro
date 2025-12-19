![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Serverless](https://img.shields.io/badge/Architecture-Serverless-blue)
![IaC](https://img.shields.io/badge/IaC-CloudFormation-brightgreen)
![Athena](https://img.shields.io/badge/Query-Athena-purple)
![Cost%20Aware](https://img.shields.io/badge/Cost-Optimized-success)
![Kiro](https://img.shields.io/badge/Built%20with-Kiro-black)

# Serverless AWS Data Lake with Kiro

Build a **cost-efficient, serverless data lake on AWS** using **S3, Glue, Athena**, and **CloudFormation**, orchestrated with **Kiro** as an agentic IDE.

This project shows how to design, deploy, and operate a **production-inspired data lake**  
— without clusters, without idle costs, and with a clean teardown.

---

## Table of Contents

1. Project Overview  
2. Architecture  
3. Kiro Features in Use  
4. Deployment Steps  
5. Cost Awareness  
6. Teardown  
7. Sample Data  
8. References  

---

## Project Overview

### Problem this project solves
- Avoid overengineering AWS data lakes  
- Prevent surprise cloud costs  
- Use serverless, batch-oriented architecture  
- Enable reproducible infrastructure with IaC  

### Tech stack
- Amazon S3 (raw + curated layers)  
- AWS Glue (crawlers + jobs)  
- Amazon Athena (SQL query engine)  
- AWS CloudFormation (infrastructure as code)  
- **Kiro** (agentic IDE: Specs, Steering, Hooks)  

---

## Architecture
<img width="1536" height="1024" alt="architecture_diagram" src="https://github.com/user-attachments/assets/e3773315-8893-4499-a1d4-16bbf70eb226" />



### Key characteristics
- Fully serverless (no EMR, no always-on compute)
- Raw / curated separation
- Parquet + partitioning for efficient queries
- CloudFormation for reproducibility and teardown

---

## Kiro Features in Use

| Feature | How it helps |
|------|-------------|
| **Specs** | Define a minimal, dev-focused data lake |
| **Steering** | Guide decisions toward serverless and cost efficiency |
| **Hooks** | Automate Glue crawlers and jobs |
| **Agentic Chat** | Conversational setup for infra and pipelines |

> Kiro helps you **think like a data engineer before you deploy**.

---

## Deployment Steps

### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/serverless-aws-data-lake-with-kiro.git
cd serverless-aws-data-lake-with-kiro
### 2. Configure AWS credentials and region
aws configure
export AWS_REGION=us-east-2
export AWS_DEFAULT_REGION=us-east-2
### 3. Deploy infrastructure
aws cloudformation deploy \
  --template-file cloudformation/data-lake-infrastructure.yaml \
  --stack-name latam-data-lake-dev \
  --capabilities CAPABILITY_NAMED_IAM \
  --tags env=dev team=data project=latam-data-lake
### 4. Upload sample raw data to S3
aws s3 cp data/raw/sample_raw.csv \
  s3://latam-data-lake-raw-dev-<ACCOUNT_ID>/orders/year=2024/month=01/
### 5. Run Glue crawlers and jobs
Trigger manually from the AWS Console

Or let Kiro Hooks automate execution

### 6. Query data with Athena
Use Athena to query curated Parquet data via the Glue Data Catalog.

## Cost Awareness
Where costs come from:

- S3: storage and requests (low, predictable)

- Glue: pay per second while jobs run

- Athena: pay per data scanned

Cost controls applied:

- Parquet + partitioning

- Serverless-only services

- Automated governance checks

- Easy teardown

## Teardown
To stop all costs:
aws cloudformation delete-stack --stack-name latam-data-lake-dev
This removes Glue, IAM roles, and automation.

Optionally delete S3 buckets if no longer needed.

## Sample Data
Sample CSV files are provided in:
data/raw/sample_raw.csv
Used to test crawlers, jobs, and Athena queries.

## References
Kiro Documentation: https://kiro.dev/docs

AWS Glue: https://aws.amazon.com/glue/

Amazon Athena: https://aws.amazon.com/athena/

AWS CloudFormation: https://aws.amazon.com/cloudformation/

⭐ If you find this repository useful, consider giving it a star.
📩 Contact: rociomnbaigorria@gmail.com
