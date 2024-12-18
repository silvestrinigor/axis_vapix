# Genetec Requests Using Python

Make requests to Axis devices using python

## Examples

### 1\. Device configuration

```python
>>> import axis.vapix.devices
>>> device = axis.vapix.devices.Device('localhost', '80', 'root', 'pass')
>>> device.time_zone
America/Sao_Paulo
>>> device.version
10.12.228
>>> from datetime import datetime
>>> device.date_time = datetime.now() # sets in device
```

### 2\. Method requests

```python
>>> import axis.vapix.methods
>>> import axis.vapix.defaults
>>> import axis.vapix.request
>>> request_maker = axis.vapix.request.AxisDefaultRequestMaker('localhost', '80', 'root', 'pass')
>>> text_overlay = axis.vapix.defaults.TextOverlay()
>>> text_overlay.text = "test"
>>> text_overlay.position = axis.vapix.defaults.OverlayPositionType.BOTTOM_RIGHT
>>> axis.vapix.methods.add_dynamic_overlay_text(request_maker, text_overlay)
```

&nbsp;