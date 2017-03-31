from concurrent import futures
import time

import grpc

import identification_pb2
import identification_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Identification(identification_pb2_grpc.IdentiteServicer):

  def Identifie(self, request, context):
    if request.name == 'toto' and request.password == 'titi':
      return identification_pb2.IdentificationReply(message=1)
    else:
      return identification_pb2.IdentificationReply(message=0)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  identification_pb2_grpc.add_IdentiteServicer_to_server(Identification(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
