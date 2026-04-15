# Release notes

<!-- do not remove -->

## 0.2.4


### Breaking Changes

- Update gauges sample to better represent real data (and update tests and example accordingly). Raise error in gauges romulo plot when irregular time index is detected. ([#57](https://github.com/rainsmore/raincell/issues/57))


## 0.2.3

### New Features

- Display missing data with a different color in gauges romulo plot ([#55](https://github.com/rainsmore/raincell/issues/55))



## 0.2.2
### Breaking Changes

- Migrate from nbdev2 to nbdev3 ([#54](https://github.com/rainsmore/raincell/pull/54))

### Bugs

- Allow plotting single gauge data in romulo plot ([#52](https://github.com/rainsmore/raincell/pull/52))


## 0.2.1

### New Features

- Add mapbox zoom and center computation functions ([#44](https://github.com/rainsmore/raincell/issues/44)
  - To be able to estimate the center and the start zoom level of some given geometries in order to be able to manually instantiate a folium.Map in the right position without the need of gdf.explore

- Allow toggling sublink metadata by default to hide it when exploring data ([#42](https://github.com/rainsmore/raincell/issues/42))



## 0.2.0

### New Features

- Create data visualization map ([#38](https://github.com/rainsmore/raincell/issues/38))
- Add grey tile to default map generation to ease visualization ([#40](https://github.com/rainsmore/raincell/issues/40))
