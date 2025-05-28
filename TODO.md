# - Implement --respect-git: ignores all ignored files via .gitignore (this is going to be harder than expected)

# - Fix error
```
-countsy --ignore --tqdm
```
`>`
 ```
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 18567/18567 [00:03<00:00, 5258.35it/s]
Errors encountered:
  - Error in ./lib/python3.13/test/tokenizedata/badsyntax_pep3120.py: 'utf-8' codec can't decode byte 0xf6 in position 8: invalid start byte
  - Error in ./lib/python3.13/test/encoded_modules/module_koi8_r.py: 'utf-8' codec can't decode byte 0xf0 in position 59: invalid continuation byte
  - Error in ./lib/python3.13/test/encoded_modules/module_iso_8859_1.py: 'utf-8' codec can't decode byte 0xe9 in position 87: invalid continuation byte
  - Error in ./lib/python3.13/site-packages/IPython/core/tests/nonascii.py: 'utf-8' codec can't decode byte 0xb1 in position 81: invalid start byte
  - Error in ./lib/python3.13/site-packages/IPython/core/tests/nonascii2.py: 'utf-8' codec can't decode byte 0xb1 in position 81: invalid start byte
  - Error in ./lib/python3.13/site-packages/joblib/test/test_func_inspect_special_encoding.py: 'utf-8' codec can't decode byte 0xa4 in position 64: invalid start byte
  - Error in ./share/doc/python3.13/examples/Tools/i18n/pygettext.py: 'utf-8' codec can't decode byte 0xfc in position 224: invalid start byte

Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.13/bin/countsy", line 8, in <module>
    sys.exit(main())
             ~~~~^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/src/cli.py", line 324, in main
    format_output(raw_output, all_python_files, args)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/src/cli.py", line 210, in format_output
    key = next(k for k in raw_output.keys() if k != "errors")
StopIteration

fix utf8 errors
```

# - Inline comments

# - Use python's inbuilt tokenizer to handle syntactically correct code and fall back to my manual checking for bad code
