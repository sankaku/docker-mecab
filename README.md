# docker-mecab
Easy tool to split words by blank with [MeCab](https://taku910.github.io/mecab/) and [NEologd](https://github.com/neologd/mecab-ipadic-neologd).

## Build
```sh
docker build . -t docker-mecab
```

## Use
### Split recursively all the files in directory, save into another directory
This script keeps the directory structure.  
e.g.) input/foo/bar/baz/1.txt -> output/foo/bar/baz/1.txt

1. Put files/directories into `./mount/input`  
  The file extension must be **txt**.
2. execute command  
  ```sh
  ./split.sh
  ```
3. You'll find the splitted files in `./mount/output`

## License
MIT License
