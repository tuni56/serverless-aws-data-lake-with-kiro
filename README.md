# Serverless AWS Data Lake with Kiro

Build a cost-efficient, serverless data lake on AWS using **S3, Glue, Athena**, and **CloudFormation**, orchestrated with **Kiro** as an agentic IDE.

This project demonstrates how to design, deploy, and operate a **full data lake** without clusters, without idle costs, and with an easy teardown process.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Architecture](#architecture)  
3. [Kiro Features in Use](#kiro-features-in-use)  
4. [Deployment Steps](#deployment-steps)  
5. [Cost Awareness](#cost-awareness)  
6. [Teardown](#teardown)  
7. [Sample Data](#sample-data)  
8. [References](#references)

---

## Project Overview

**Problem solved:**
- Avoid overengineering AWS data lakes  
- Prevent surprise cloud costs  
- Implement serverless architecture with batch processing  
- Enable reproducible, deployable infrastructure  

**Tech stack:**
- AWS S3 (raw + curated)  
- AWS Glue (crawlers + jobs)  
- AWS Athena (query engine)  
- CloudFormation (infrastructure as code)  
- **Kiro** (agentic IDE for Specs, Steering, Hooks)  

---

## Architecture

<img width="1536" height="1024" alt="architecture_diagram" src="https://github.com/user-attachments/assets/54c9b7d2-fb6e-4c32-a90d-9903e9674451" />

**Highlights:**
- Serverless: no EMR clusters, no always-on compute  
- Raw / Curated separation for structured workflows  
- Parquet + partitioning for query efficiency  
- CloudFormation ensures reproducibility and easy teardown  

*See `docs/architecture.png` for a visual diagram.*

---

## Kiro Features in Use

| Feature       | How It Helps |
|---------------|-------------|
| **Specs**     | Structured plan for minimal dev lake |
| **Steering**  | Guides AI to serverless, cost-efficient decisions |
| **Hooks**     | Automates Glue crawlers and job triggers |
| **Agentic Chat** | Conversational interface for infrastructure & pipeline setup |

> Kiro helps you **think like a data engineer** before you deploy code.

---

## Deployment Steps

1. Clone repo  
   ```bash
   git clone https://github.com/YOUR_USERNAME/serverless-aws-data-lake-with-kiro.git
   cd serverless-aws-data-lake-with-kiro
Configure AWS credentials & region

aws configure
export AWS_REGION=us-east-2
export AWS_DEFAULT_REGION=us-east-2


Deploy infrastructure

aws cloudformation deploy \
    --template-file infra/data-lake-infrastructure.yaml \
    --stack-name latam-data-lake-dev \
    --capabilities CAPABILITY_NAMED_IAM \
    --tags env=dev team=data project=latam-data-lake


Upload sample raw data to S3

Trigger Glue crawlers & jobs (or let Hooks automate)

Query data with Athena

## Cost Awareness

S3: storage + requests (cheap)

Glue: pay per second while jobs run

Athena: pay per data scanned (optimize with Parquet + partitions)

Hooks ensure Glue jobs only run when needed, minimizing idle cost.

## Teardown

To stop costs completely:

aws cloudformation delete-stack --stack-name latam-data-lake-dev


This deletes Glue resources and infrastructure.

S3 buckets can be deleted if no longer needed.

See teardown/destroy.md for details.

Sample Data

Included in data/sample/raw_sample.csv for testing crawlers and transformations.

## References

Kiro Documentation: https://kiro.dev/docs/ 

AWS Glue: https://aws.amazon.com/glue/

AWS Athena: https://aws.amazon.com/athena/ 

AWS CloudFormation: https://aws.amazon.com/cloudformation/ 

## If you find this repo useful give it an star.
## Feel free to reach out at: rociomnbaigorria@gmail.com
