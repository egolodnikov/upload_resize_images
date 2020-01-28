# upload_resize_images
Description:
Страница содержит изображение. Если нет GET-параметров, то оно приходит с бэка неизменённым. Могут присутствовать два GET-параметра:
  - width - ширина
  - height - высота
  
Они могут присутствовать как по отдельности, так и вместе.

При наличии параметром производится ресайз изображения. Исходное изображение не меняется. Используется кэширование, чтобы не генерировалось новое изображение при повторных запросах.

install:
docker-compose up
