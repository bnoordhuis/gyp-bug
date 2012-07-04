{
  'targets': [
    {
      'target_name': 'b',
      'type': 'executable',
      'sources': ['b.c'],
      'dependencies': ['../a/build.gyp:a'],
    }
  ]
}
