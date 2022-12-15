from custominterface_serializer import AddSerializer
from mlem.api import serve





def main():
    serve("../model/clf-model", "fastapi", request_serializer=AddSerializer())


if __name__ == '__main__':
    main()