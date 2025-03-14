
@rescui/use-glow-hover Documentation
====================================

## useGlowHover

### Description


This module exports the `useGlowHover` hook, which is used to add a glow effect to an HTML element when it is hovered over. It also exports some utility functions for working with themes.
### Parameters

#### options

##### Type


GlowHoverHookOptions
##### Description


An object containing the options for the glow effect. See [GlowHoverOptions](#glowhoveroptions) for details.
### Return Value

#### ref

##### Type


MutableRefObject<HTMLElement>
##### Description


A mutable ref that points to the element with the glow effect.
### Example Use
```ts 
import React from 'react'; import useGlowHover from '@rescui/use-glow-hover'; function MyComponent() { const hoverRef = useGlowHover(); return ( <> <div ref={hoverRef}>Hover me!</div> </> ); }
```
### Test Cases

#### Simple usage

##### Description


A basic test to ensure the hook works correctly.
##### Code
```ts 
import React from 'react'; import useGlowHover from '@rescui/use-glow-hover'; it('renders a glow effect on hover', () => { const { getByText } = render(<MyComponent />); const div = getByText('Hover me!'); fireEvent.mouseOver(div); expect(div).toHaveAttribute('style', 'background-color: red;'); });
```

 --- 

## GlowHoverHookOptions

### Description


The `glowHoverEffect` function is used to create a glow effect on an element when hovered. It takes in an HTMLElement and options for the effect, returning a function that can be called to remove the effect.
### Parameters

#### el

##### Type


HTMLElement
##### Description


The element to apply the hover effect to.

 --- 

#### options

##### Type


{ preset, ...GlowHoverOptions }
##### Description


Options for the glow effect. Can include a preset and other GlowHoverOptions such as hover background color or animation speed.
### Return Value

#### () => void

##### Type


Function
##### Description


A function that can be called to remove the glow effect.
### Example Use
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';

const button = document.getElementById('button');
const stopGlow = glowHoverEffect(button, {
  preset: 'default',
  hoverBg: '#333',
});

// To remove the glow effect later
stopGlow();
```
### Test Cases

#### Basic Glow Effect

##### Description


Create a basic glow effect on an element.
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
const button = document.getElementById('button');
const stopGlow = glowHoverEffect(button);

// To remove the glow effect later
stopGlow();
```

 --- 

#### Custom Glow Effect

##### Description


Create a custom glow effect with specific options.
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
const button = document.getElementById('button');
const stopGlow = glowHoverEffect(button, {
  preset: 'custom',
  hoverBg: '#333',
});

// To remove the glow effect later
stopGlow();
```

 --- 

## glowHoverEffect

### Description


The `glowHoverEffect` function creates a glowing hover effect on an HTML element.
### Parameters

#### el

##### Type


HTMLElement
##### Description


The HTML element to apply the glow hover effect to

 --- 

#### options

##### Type


{ preset, ...GlowHoverOptions }
##### Description


An object containing options for the glow hover effect. See `GlowHoverOptions` type for available options.
### Return Value

#### function

##### Type


() => void
##### Description


A function that can be used to cleanup or cancel the glow hover effect
### Example Use
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover'; const element = document.getElementById('myElement'); glowHoverEffect(element, { preset: 'default', forceTheme: 'dark' });
```
### Test Cases

#### Basic usage

##### Description


Apply the default glow hover effect to an element
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover'; const element = document.getElementById('myElement'); glowHoverEffect(element);
```

 --- 

#### With preset

##### Description


Apply a specific preset to an element
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover'; const element = document.getElementById('myElement'); glowHoverEffect(element, { preset: 'custom' });
```

 --- 

#### With forceTheme

##### Description


Force a theme on hover
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover'; const element = document.getElementById('myElement'); glowHoverEffect(element, { forceTheme: 'light' });
```

 --- 

## GlowHoverOptions

### Description


This export provides an options object for customizing the glow hover effect.
### Parameters

#### hoverBg

##### Type


string
##### Description


Background color on hover

 --- 

#### lightSize

##### Type


number
##### Description


Size of the light on hover

 --- 

#### lightSizeEnterAnimationTime

##### Type


number
##### Description


Time for animation to enter

 --- 

#### lightSizeLeaveAnimationTime

##### Type


number
##### Description


Time for animation to leave

 --- 

#### isElementMovable

##### Type


boolean
##### Description


Whether the element is movable on hover

 --- 

#### customStaticBg

##### Type


string
##### Description


Custom static background color

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


Whether to enable burst effect

 --- 

#### mode

##### Type


'glow' | 'sharp'
##### Description


Animation mode
### Return Value

#### () => void

##### Type


function
##### Description


Returns a function that will be called on hover
### Example Use
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
```
### Test Cases

#### Basic test case

##### Description


This test case checks if the effect is applied correctly
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
```

 --- 

#### Hover background color test case

##### Description


This test case checks if the hover background color is applied correctly
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
```

 --- 

#### Light size animation time test case

##### Description


This test case checks if the light size animation time is applied correctly
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
```

 --- 

#### Test force theme option

##### Description


This test case checks if the force theme option is applied correctly
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
```

 --- 

#### Test enable burst option

##### Description


This test case checks if the enable burst option is applied correctly
##### Code
```ts 
import { glowHoverEffect } from '@rescui/use-glow-hover';
```