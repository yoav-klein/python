import argparse


def index(args):
    def create():
        print(f"Creating {args.name}")

    def delete():
        print(f"Deleting {args.name}")

    if args.subcommand == "delete":
        delete()
    
    if args.subcommand == "create":
        create()

def document(args):
    pass


def parse_arguments():
    # Create the top-level parser
    parser = argparse.ArgumentParser(description='My Elasticsearch tool')

    subparsers = parser.add_subparsers(title='Elasticsearch commands', dest='command')
    subparsers.required = True

    # Add a subparser for the "index" command
    index_parser = subparsers.add_parser('index', help='Do index operations')

    index_subparsers = index_parser.add_subparsers(title='Index commands', dest='subcommand')
    index_subparsers.required = True

    index_create_parser = index_subparsers.add_parser('create', help="Create index")
    index_create_parser.add_argument('--name', required=True, help="Name of index")

    index_delete_parser = index_subparsers.add_parser('delete', help="Delete index")
    index_delete_parser.add_argument('--name', required=True, help="Name of index")
    
    index_parser.set_defaults(func=index)


    # Add a subparser for the "document" command
    document_parser = subparsers.add_parser('document', help='Do document operations')

    document_subparsers = document_parser.add_subparsers(title="Document commands", dest='subcommand')

    document_create_parser = document_subparsers.add_parser('create', help="Create document")
    document_create_parser.add_argument('--name', required=True, help="Name of document")

    document_delete_parser = document_subparsers.add_parser('delete', help="Delete document")
    document_delete_parser.add_argument('--name', required=True, help="Name of document")
    
    document_parser.set_defaults(func=document)

    # Parse the command-line arguments
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_arguments()
    args.func(args)


