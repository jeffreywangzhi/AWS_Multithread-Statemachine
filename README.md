# AWS_Multithread-Statemachine
A fast, efficient, multithreaded download machine based on AWS.
1. 10 respective threads (lambda function) download files from file url.
2. 10 threads upload repective chunk to target S3 bucket.
3. Job finished.
* Average System Efficiency: **1.5 GB/ second**
* Scalability: scalable with additional threads (lambda function)
![stepfunctions_graph.png](stepfunctions_graph.png)
### Input Format
```json
{
  "src": [
    {
      "filePath": "https://targetFile1.mkv"
    },
    {
      "filePath": "https://targetFile2.mkv"
    }
  ]
}
```
## Author <a name = "author"></a>
- Jeffrey Wang (jeffrey.wanggg@gmail.com)

