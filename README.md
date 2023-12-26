# AWS_Multithread-Statemachine
A fast, scalable, multithreaded download statemachine based on AWS.
1. 10+ respective threads (lambda functions) download files from target file URL.
2. 10+ threads upload each chunk to the target S3 bucket.
3. Chunk merged and job finished.
* System Efficiency: **300 GB/ minute**
* Scalability: scalable with additional threads (AWS Lambda Functions)
![statemachine_graph.png](src/statemachine/statemachine_graph.png)
## Prerequisites <a name = "prerequisites"></a> ##
* Install AWS CLI : [installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* Install AWS SAM CLI : [installation guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
* AWS Account Credentials : [How to guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)
## CloudFormation Template Configuration <a name = "config"></a> ##
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
$ Parameter TargetS3 [targetS3]: your-target-storage-s3-name
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
## Scalability <a name = "build"></a> ##
With above solution, the system efficiency achieved 300 GB per minute. The scalable system could also be further refined by thresholding the lambda functions (threads).
## Who do I talk to <a name = "author"></a>
- Jeffrey Wang (jeffreywangzhi@gmail.com)

