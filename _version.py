import json

version_json = '''
{
 "date": "2024-01-14T14:33:22+0600",
 "dirty": false,
 "error": null,
 "full-revisionid": "1ff32de4c4f4b50e1d922763ae88b3cb677c52b0",
 "version": "1.0"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
