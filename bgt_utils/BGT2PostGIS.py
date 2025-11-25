#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import pathlib

import utils as bgt_utils

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description = "Imports a BGT zip file as downloaded from the "
                      "BGT dowload site into PostGIS."
    )

    parser.add_argument(    
        "-H", 
        "--host", 
        default = '',
        help = "database server host"
    )
    parser.add_argument(    
        "-p", 
        "--port", 
        default = 5432,
        help = "database server port"
    )
    parser.add_argument(    
        "-U", 
        "--username", 
        help = "database user name"
    )
    parser.add_argument(    
        "-W", 
        "--password", 
        help = "database user password"
    )
    parser.add_argument(
        "-d",
        "--dbname",
        help = "database name to connect to"
    )
    parser.add_argument(
        "-s",
        "--schema",
        help = "existing database schema to store the data",
        default = "public"
    )
    parser.add_argument(
        "zip_file",
        type = pathlib.Path, 
        help = "The BGT zip file."
    )
    
    args = parser.parse_args()

connection_string = "PG: host='%s' port='%s' dbname='%s'" % (
                        args.host,
                        args.port,
                        args.dbname )

if args.username:
    connection_string = connection_string + " user='%s'" % args.username
if args.password:
    connection_string = connection_string + " password='%s'" % args.password
                        
no_exceptions = bgt_utils.import_to_postgis(
    task = None,
    zip_file_name = args.zip_file,
    connection_string = connection_string,
    schema = args.schema)

