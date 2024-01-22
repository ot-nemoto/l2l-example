# r6jan-example

- Lambda(invoker-app) から Lambda(invokee-app) を呼び出す

## Environment

```sh
python --version
  # Python 3.10.13
sam --version
  # SAM CLI, version 1.107.0
```

## Deploy

### invokee-app

```sh
cd invokee-app

sam build

sam deploy \
  --parameter-overrides SecurityGroupIds=SECURITY_GROUP_IDS \
                        SubnetIds=SUBNET_IDS
```

**Parameters**

|Parameter|Type|Description|Default|
|--|--|--|--|
|SecurityGroupIds|String|セキュリティグループID<br>複数の場合はカンマ区切り<br>SecurityGroupIdsを指定する場合は。SubnetIdsの指定も必須|-|
|SubnetIds|String|サブネットID<br>複数の場合はカンマ区切り<br>SubnetIdsを指定する場合は。SecurityGroupIdsの指定も必須|-|

### invoker-app

```sh
cd invoker-app

sam build

sam deploy \
  --parameter-overrides SecurityGroupIds=SECURITY_GROUP_IDS \
                        SubnetIds=SUBNET_IDS \
                        InvokeeFunctionArn=INVOKEE_FUNCTION_ARN
```

**Parameters**

|Parameter|Type|Description|Default|
|--|--|--|--|
|SecurityGroupIds|String|セキュリティグループID<br>複数の場合はカンマ区切り<br>SecurityGroupIdsを指定する場合は。SubnetIdsの指定も必須|-|
|SubnetIds|String|サブネットID<br>複数の場合はカンマ区切り<br>SubnetIdsを指定する場合は。SecurityGroupIdsの指定も必須|-|
|InvokeeFunctionArn|String|invokee-app(Lambda)のARN|-|