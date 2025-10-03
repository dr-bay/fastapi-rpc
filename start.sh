#!/bin/bash
uvicorn RPC:app --host 0.0.0.0 --port $PORT

