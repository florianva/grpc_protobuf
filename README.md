# grpc_protobuf
This project is a simple client server with gRPC/Protobuf

####Step 1
Install gRPC and gRPC tools
```
$ python -m pip install grpcio
$ python -m pip install grpcio-tools
```

####Step 2
Define message format in a .proto file
For example : 

```
syntax = "proto3";

//Identification service definition
service Identite {
  rpc Identifie (IdentificationRequest) returns (IdentificationReply) {}
}

message IdentificationRequest {
  string name = 1;
  string password = 2;
}

message IdentificationReply {
  int32 message = 1;
}
```
####Step 3
Generate the class and stub class from you're .proto file 
```
$ python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. identification.proto

```
This generates "identification_pb2.py" and "identification_pb2_grpc.py"  in your specified destination directory. 

####Step 4
Run the server
```
$ python server.py
```

In another terminal, run the client
```
$ python client.py
```

Congratulations! You’ve just run a client-server application with gRPC.