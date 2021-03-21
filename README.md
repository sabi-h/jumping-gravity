# nPlan
Data Engineering assessment for nPlan


### Current Architecture
![Current Architecture](./docs/current_architecture.png)


### Future Architecture
![Future Architecture](./docs/future_architecture.png)


#### Setup


##### Create .env file in project root and set the following variables
```
PUBLISHABLE_TOKEN=[IEX_PUBLISHABLE_TOKEN]
PROJECT_ID=[GCP_PROJECT_ID]
GOOGLE_APPLICATION_CREDENTIALS=[GOOGLE_APPLICATION_CREDENTIALS]
```

##### Service Account
- Put service account file `service_account.json` with write access to your BigQuery dataset.


##### Start streaming data into BigQuery
```
git clone https://github.com/sabih-h/jumping-gravity.git
cd jumping-gravity
python main.py
```


##### Info
- Tested on python version 3.7.9