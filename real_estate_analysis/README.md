# Исследование продаж недвижимости

## Данные 
- `locality_name` — название населённого пункта
- `cityCenters_nearest` — расстояние до центра города (м)
- `airports_nearest` — расстояние до ближайшего аэропорта в метрах (м)
- `parks_around3000` — число парков в радиусе 3 км
- `parks_nearest` — расстояние до ближайшего парка (м)
- `ponds_around3000` — число водоёмов в радиусе 3 км
- `ponds_nearest` — расстояние до ближайшего водоёма (м)
- `total_area` — общая площадь квартиры в квадратных метрах (м²)
- `living_area` — жилая площадь в квадратных метрах (м²)
- `kitchen_area` — площадь кухни в квадратных метрах (м²)
- `ceiling_height` — высота потолков (м)
- `floors_total` — всего этажей в доме
- `floo`r` — этаж
- `rooms` — число комнат
- `studio` — квартира-студия (булев тип)
- `open_plan` — свободная планировка (булев тип)
- `balcony` — число балконов
- `is_apartment` — апартаменты (булев тип)
- `total_images` — число фотографий квартиры в объявлении
- `first_day_exposition` — дата публикации
- `last_price` — цена на момент снятия с публикации
- `days_exposition` — сколько дней было размещено объявление (от публикации до снятия)

## Задача
Задача — выполнить предобработку данных и изучить их, чтобы найти интересные особенности и зависимости, которые существуют на рынке недвижимости.
О каждой квартире в базе содержится два типа данных: добавленные пользователем и картографические. Например, к первому типу относятся площадь квартиры, её этаж и количество балконов, ко второму — расстояния до центра города, аэропорта и ближайшего парка. 

## Библиотеки
- pandas
- matplotlib
- seaborn