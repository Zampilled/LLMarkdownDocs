
@rescui/use-glow-hover Documentation
====================================

## useGlowHover

### Description


The `useGlowHover` hook is a React hook that enables glow hover effect on an element. It takes options as an argument to customize the appearance and behavior of the glow hover effect.
### Parameters

#### disabled

##### Type


boolean
##### Description


A boolean value indicating whether the glow hover effect is disabled or not.

 --- 

#### options

##### Type


GlowHoverOptions
##### Description


An object containing options to customize the appearance and behavior of the glow hover effect.
### Return Value

#### ref

##### Type


MutableRefObject<HTMLElement>
##### Description


A reference to the element that is being hovered by the glow hover effect.
### Example Use
```ts 
import { useGlowHover } from '@rescui/use-glow-hover';

const App = () => {
  const ref = useGlowHover({ preset: 'light', lightColor: '#ff0000' });

  return <div>
    <p ref={ref}>Hello World!</p>
  </div>
};
```
### Test Cases

#### Test disabled option

##### Description


Test if the glow hover effect is disabled when the `disabled` option is set to `true`.
##### Code
```ts 
import { useGlowHover } from '@rescui/use-glow-hover';

const App = () => {
  const ref = useGlowHover({ disabled: true });

  return <div>
    <p ref={ref}>Hello World!</p>
  </div>
};
```

 --- 

#### Test default options

##### Description


Test if the glow hover effect is enabled with default options.
##### Code
```ts 
import { useGlowHover } from '@rescui/use-glow-hover';

const App = () => {
  const ref = useGlowHover();

  return <div>
    <p ref={ref}>Hello World!</p>
  </div>
};
```

 --- 

#### Test custom options

##### Description


Test if the glow hover effect is enabled with custom options.
##### Code
```ts 
import { useGlowHover } from '@rescui/use-glow-hover';

const App = () => {
  const ref = useGlowHover({ preset: 'dark', lightColor: '#00ff00' });

  return <div>
    <p ref={ref}>Hello World!</p>
  </div>
};
```

 --- 

## GlowHoverHookOptions

### Description


The GlowHoverHookOptions type defines the options for the glow hover effect. It includes various properties to customize the appearance and behavior of the effect.
### Parameters

#### hoverBg

##### Type


string
##### Description


The background color of the hover element.

 --- 

#### lightSize

##### Type


number
##### Description


The size of the light effect.

 --- 

#### lightSizeEnterAnimationTime

##### Type


number
##### Description


The animation time for entering the light effect.

 --- 

#### lightSizeLeaveAnimationTime

##### Type


number
##### Description


The animation time for leaving the light effect.

 --- 

#### isElementMovable

##### Type


boolean
##### Description


Whether the hover element is movable or not.

 --- 

#### customStaticBg

##### Type


string
##### Description


A custom static background color for the hover element.

 --- 

#### forceTheme

##### Type


'light' | 'dark' | false
##### Description


Force theme on hover. Use with caution.

 --- 

#### enableBurst

##### Type


boolean
##### Description


Enable burst mode.

 --- 

#### mode

##### Type


'glow' | 'sharp'
##### Description


The glow or sharp mode. @default glow
### Return Value

#### GlowHoverOptions

##### Type


(string | number)[]
##### Description


This function parses a color string into an array of string and number values.
### Example Use
```ts 
const parsedColor = parseColor('#ff0000'); // ['#FF0000', 255, 0, 0]
```
### Test Cases

#### Test parsing a valid color

##### Description


Test if the function correctly parses a valid color string.
##### Code
```ts 
const parsedColor = parseColor('#ff0000'); // ['#FF0000', 255, 0, 0]
```

 --- 

#### Test parsing an invalid color

##### Description


Test if the function correctly handles an invalid color string.
##### Code
```ts 
const result = parseColor('invalid-color'); expect(result).toEqual([]);
```

 --- 

## glowHoverEffect

### Description


The glowHoverEffect function applies a glow hover effect to an HTML element.
### Parameters

#### el

##### Type


HTMLElement
##### Description


The HTML element to apply the glow hover effect to.

 --- 

#### options

##### Type


GlowHoverOptions
##### Description


An object containing options for the glow hover effect.
### Return Value

#### 

##### Type


() => void
##### Description


A function that returns a cleanup function to remove the glow hover effect from the element.
### Example Use
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
const element = document.getElementById('myElement');
glowHoverEffect(element, {
  preset: 'myPreset',
  hoverBg: '#333'
});
```
### Test Cases

#### Default Glow Hover Effect

##### Description


Apply the default glow hover effect to an element.
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
const element = document.getElementById('myElement');
glowHoverEffect(element);

```

 --- 

#### Custom Glow Hover Effect

##### Description


Apply a custom glow hover effect to an element.
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
const element = document.getElementById('myElement');
glowHoverEffect(element, {
  preset: 'myPreset',
  hoverBg: '#333'
});

```

 --- 

## GlowHoverOptions

### Description


The GlowHoverOptions type defines the properties that can be used to customize the glow hover effect.
### Parameters

#### hoverBg

##### Type


string
##### Description


The background color of the glow on hover.

 --- 

#### lightSize

##### Type


number
##### Description


The size of the light when it's hovered over.

 --- 

#### lightSizeEnterAnimationTime

##### Type


number
##### Description


The time it takes for the light to enter its new size during animation.

 --- 

#### lightSizeLeaveAnimationTime

##### Type


number
##### Description


The time it takes for the light to leave its current size during animation.

 --- 

#### isElementMovable

##### Type


boolean
##### Description


Whether the element can be moved around while hovered over.

 --- 

#### customStaticBg

##### Type


string
##### Description


The static background color of the glow when it's not hovered over.

 --- 

#### forceTheme

##### Type


'light' | 'dark' | false
##### Description


Forces the theme on hover. Use with caution. Default is undefined.

 --- 

#### enableBurst

##### Type


boolean
##### Description


Whether to enable the burst effect. Default is false.

 --- 

#### mode

##### Type


'glow' | 'sharp'
##### Description


The mode of the glow hover effect. Default is undefined.
### Return Value

#### 

##### Type


(string | number)[]
##### Description


An array containing the color codes for parsing and string or number values if no parsing is required
### Example Use
```ts
import { glowHoverEffect } from '@rescui/use-glow-hover';
const element = document.getElementById('myElement');
glowHoverEffect(element, {
    hoverBg: 'rgba(0, 0, 0, 0.2)',
    lightSize: 100,
    lightSizeEnterAnimationTime: 200,
    isElementMovable: true,
});
```
### Test Cases

#### Hover over element with default settings

##### Description


Test the glow hover effect when hovering over an element with default settings.
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
const element = document.getElementById('myElement');
glowHoverEffect(element);

```

 --- 

#### Hover over element with custom hover background

##### Description


Test the glow hover effect when hovering over an element with a custom hover background.
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
const element = document.getElementById('myElement');
glowHoverEffect(element, {
    hoverBg: 'rgba(0, 0, 0, 0.2)',
});

```

 --- 

#### Enable burst effect

##### Description


Test the glow hover effect when enabling the burst effect.
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
const element = document.getElementById('myElement');
glowHoverEffect(element, {
    enableBurst: true,
});

```

 --- 

#### Force dark theme

##### Description


Test the glow hover effect when forcing a dark theme.
##### Code
```ts 
import { forceDarkTheme } from '@rescui/use-glow-hover';
const element = document.getElementById('myElement');
forceDarkTheme(element);

```