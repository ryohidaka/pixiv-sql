# Changelog

## [0.2.0](https://github.com/ryohidaka/pixiv-sql/compare/v0.1.0...v0.2.0) (2024-05-13)


### Features

* Add "create_date" column to bookmarks table. ([4a57e56](https://github.com/ryohidaka/pixiv-sql/commit/4a57e5603a5dea6d344d4591e32d18bc5de50632))
* Add "is_private" column to bookmarks table. ([96c1adc](https://github.com/ryohidaka/pixiv-sql/commit/96c1adc9928018454b97c42f1bf21ed5d8d97572))
* Add foreign key constraint to bookmarks table. ([fadaf86](https://github.com/ryohidaka/pixiv-sql/commit/fadaf86af184857a27394d05462af5d7bf36b116))
* Add function to create images table. ([1741562](https://github.com/ryohidaka/pixiv-sql/commit/1741562c5ec901c731216fa6a8ee8be74c79fd9c))
* Add function to create types table. ([de97567](https://github.com/ryohidaka/pixiv-sql/commit/de97567ec61ee199d8cdad5ce8409ea39180d163))
* Add function to insert images. ([6b9c93f](https://github.com/ryohidaka/pixiv-sql/commit/6b9c93f589d1faad2b457694332ae3caa91af8ce))
* Modified "type" column on bookmarks table to "type_id" . ([00d5fea](https://github.com/ryohidaka/pixiv-sql/commit/00d5feab0fa375b1ff4ee4b681fa76d59986f881))
* Rename bookmark file to illust. ([7704107](https://github.com/ryohidaka/pixiv-sql/commit/77041072d3ae6db7592e8379f8e1d0b009fc3f89))


### Bug Fixes

* Fixed to ignore duplicate inserts. ([8dca91a](https://github.com/ryohidaka/pixiv-sql/commit/8dca91a6e1449357d191e4650cae7ebc8fa61bc1))
* Remove unneeded sleep(). ([c994bdc](https://github.com/ryohidaka/pixiv-sql/commit/c994bdc4aae92c4d22d99ff7516e800d56cd0517))


### Documentation

* Fix Changelog url. ([2693d7a](https://github.com/ryohidaka/pixiv-sql/commit/2693d7a77e2379e32f94429c9fae45012de5f4d1))
* Update README ([cf02452](https://github.com/ryohidaka/pixiv-sql/commit/cf02452eb6a2c0a45ef9fefa7aa43661932b1fb0))
* Update README ([7e3217a](https://github.com/ryohidaka/pixiv-sql/commit/7e3217a53fc8c4e0298348f65a00e64eace5cb36))

## 0.1.0 (2024-05-12)


### Features

* Add DB ([98e3aa4](https://github.com/ryohidaka/pixiv-sql/commit/98e3aa4415b152c16549fa62e08df659ab3e22fe))
* Add function to create bookmark table. ([81527b0](https://github.com/ryohidaka/pixiv-sql/commit/81527b0a554023c8dc5cded185af11e6211f35ae))
* Add function to create bookmarks_tags table. ([a9e54bb](https://github.com/ryohidaka/pixiv-sql/commit/a9e54bbdd9c194bb32e6307ccd0df81641c6b144))
* Add function to create tags table. ([59b143a](https://github.com/ryohidaka/pixiv-sql/commit/59b143a057bd36a106f79e74e1d58f7104f46205))
* Add function to create users table. ([d8881ae](https://github.com/ryohidaka/pixiv-sql/commit/d8881aeb2302e86d469079d979c07efc7c34a0c4))
* Add function to insert bookmarks_tags. ([8f07a39](https://github.com/ryohidaka/pixiv-sql/commit/8f07a39e0bcd61cf635f374eb9304be2adeffec0))
* Add function to insert bookmarks. ([4c42745](https://github.com/ryohidaka/pixiv-sql/commit/4c427451abb231a7b880f82a3d92c281b8d45a00))
* Add function to insert into table. ([78e5622](https://github.com/ryohidaka/pixiv-sql/commit/78e562292820d147ee443e5f01ac87c24916dd68))
* Add function to insert tags. ([eec8568](https://github.com/ryohidaka/pixiv-sql/commit/eec8568d545cbc430149384fd92e7373248975e1))
* Add function to insert users. ([dfea221](https://github.com/ryohidaka/pixiv-sql/commit/dfea22192915c77f631a3e87d8f64e9b87049b26))
* Add initializer for pixivpy. ([c720aa7](https://github.com/ryohidaka/pixiv-sql/commit/c720aa7e65bbd26c67ff7d3914b1e2f77b33b8e3))
* Add logger. ([087c438](https://github.com/ryohidaka/pixiv-sql/commit/087c43822dc9d57308802c6e931e75779efdc583))
* Add process to get user bookmarks. ([cbf0f08](https://github.com/ryohidaka/pixiv-sql/commit/cbf0f0834702829e2d3c03f388c26fd0a033d86f))
* Install dotenv ([95e4ab1](https://github.com/ryohidaka/pixiv-sql/commit/95e4ab1f31b0b6fc53feeb5f5995119282169eaa))
* Install Pixivpy3 ([9c80fe5](https://github.com/ryohidaka/pixiv-sql/commit/9c80fe51b7a7ae66f3976448ac3073c00669e295))


### Documentation

* Enable release-please ([68d2326](https://github.com/ryohidaka/pixiv-sql/commit/68d2326fe603507ee83811a4856e60769c8c961f))
* Update pyproject.toml ([f2e5bc9](https://github.com/ryohidaka/pixiv-sql/commit/f2e5bc950117612e2915f9eda08d777ffdc4ad39))
* Update README ([c4ef939](https://github.com/ryohidaka/pixiv-sql/commit/c4ef939081b335125eb3a247683cde1d8c4e1d15))


### Miscellaneous Chores

* release 0.1.0 ([69d8c2e](https://github.com/ryohidaka/pixiv-sql/commit/69d8c2eb68920b5c6cfe67b4d488c2aa6d1f87d6))
