# AWS_Multithread-Statemachine
A fast, scalable, multithreaded download statemachine based on AWS.
1. 10 respective threads (lambda functions) download files from the file URL.
2. 10 threads upload respective chunks to the target S3 bucket.
3. Job finished.
* System Efficiency: **300 GB/ minute**
* Scalability: scalable with additional threads (AWS Lambda Functions)
![statemachine_graph.png](src/statemachine/statemachine_graph.png)

## Prerequisites <a name = "prerequisites"></a> ##

* Install AWS CLI : [installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* Install AWS SAM CLI : [installation guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
* AWS Account Credentials : [How to guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)

## Configuration <a name = "config"></a> ##

* Replace each **aws-account** in template.yaml with your own AWS account number. (Ctrl + F, aws-account)
* Config each **Role** in StepFunctions and Lambda Functions and grant corresponding permissions. (Ctrl + F, Role)

## Building <a name = "build"></a> ##
* Build the sam application.
```bash
$ sam build
```
```bash
$ sam deploy --guided
```
* Enter your target S3 name for storing the downloaded file.
```bash
$ Parameter TargetS3 [targetS3]: your-s3-name
```

## Usage & Input Format
```json
{
  "src": [
    {
      "filePath": "https://download-file-1.ext"
    },
    {
      "filePath": "https://download-file-2.ext"
    },
    {
      "filePath": "{other-file-paths}"
    }
  ]
}
```
## Who do I talk to <a name = "author"></a>
- Jeffrey Wang (jeffrey.wanggg@gmail.com)

