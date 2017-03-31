from __future__ import print_function

import grpc

import identification_pb2
import identification_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = identification_pb2_grpc.IdentiteStub(channel)
  identification = stub.Identifie(identification_pb2.IdentificationRequest(name='toto', password = 'titi'))
  print("Reception : " + str(identification.message))



if __name__ == '__main__':
  run()
