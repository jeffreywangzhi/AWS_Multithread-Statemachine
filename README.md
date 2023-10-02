# AWS_Multithread-Statemachine
A fast, efficient, multithreaded download statemachine based on AWS.
1. 10 respective threads (lambda functions) download files from the file URL.2
2. 10 threads upload respective chunks to the target S3 bucket.
3. Job finished.
* Average System Efficiency: **1.5 GB/ second**
* Scalability: scalable with additional threads (lambda functions)
![statemachine_graph.png](src/statemachine_graph.png)
### Input Format
```json
{
  "src": [
    {
      "filePath": "https://targetFile1.mkv"
    },
    {
      "filePath": "https://targetFile2.mkv"
    },
    {
      "filePath": "{other-file-paths}"
    }
  ]
}
```
## Who do I talk to <a name = "author"></a>
- Jeffrey Wang (jeffrey.wanggg@gmail.com)

