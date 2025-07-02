#!/bin/bash
npm run build --prefix streamlit_keycloak_component/frontend  \
    && rm -rf dist/*                                \
    && python setup.py sdist bdist_wheel