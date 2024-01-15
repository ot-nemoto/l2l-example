# l2l-example

- Lambda から Lambda を呼び出すサンプル

## Environment

```sh
python --version
  # Python 3.10.13
sam --version
  # SAM CLI, version 1.107.0
```

## Deploy

|Parameter|Type|Description|Default|
|--|--|--|--|
|SecurityGroupIds|String|セキュリティグループID<br>複数の場合はカンマ区切り<br>SecurityGroupIdsを指定する場合は。SubnetIdsの指定も必須|-|
|SubnetIds|String|サブネットID<br>複数の場合はカンマ区切り<br>SubnetIdsを指定する場合は。SecurityGroupIdsの指定も必須|-|

### invokee-app

```sh
cd invokee-app

sam build

sam deploy \
  --parameter-overrides SecurityGroupIds=SECURITY_GROUP_IDS \
                        SubnetIds=SUBNET_IDS
```

### invoker-app

```sh
cd invoker-app

sam build

sam deploy \
  --parameter-overrides SecurityGroupIds=SECURITY_GROUP_IDS \
                        SubnetIds=SUBNET_IDS
```