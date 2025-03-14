
@rescui/use-glow-hover Documentation
====================================

## useGlowHover

### Description


This function is used to apply a glow hover effect to an HTML element.
### Parameters

#### el

##### Type


HTMLElement
##### Description


The target HTML element to which the glow effect will be applied.

 --- 

#### options

##### Type


GlowHoverOptions
##### Description


Configuration options for the glow hover effect, including preset settings and various parameters like light color, size, animations, etc.
### Return Value

#### 

##### Type


() => void
##### Description


A function that can be called to clean up and remove the glow effect from the element.
### Example Use
```ts
import { useState, useEffect } from 'react';
import { glowHoverEffect } from '@rescui/use-glow-hover';

export const MyComponent = () => {
  const [el] = useState<HTMLDivElement>(null);

  useEffect(() => {
    if (el) {
      glowHoverEffect(el, {
        preset: 'glassMorph',
        lightColor: '#ffffff',
        lightSize: 30,
        enableBurst: true,
      });
    }
  }, [el]);

  return <div ref={el} className="my-component" />;
};
```
### Test Cases

#### Basic Test Case

##### Description


Tests applying the glow effect with default options.
##### Code
```ts 

import { glowHoverEffect } from '@rescui/use-glow-hover';

const element = document.createElement('div');

// Apply glow hover effect with basic configuration
glowHoverEffect(element, {
  preset: 'glassMorph',
  lightColor: '#ffffff'
});

// Cleanup function
element.remove();

```

 --- 

#### Advanced Configuration Test Case

##### Description


Tests applying the glow effect with custom settings including animations.
##### Code
```ts 

import { glowHoverEffect } from '@rescui/use-glow-hover';

const element = document.createElement('div');

// Apply glow hover effect with advanced configuration
glowHoverEffect(element, {
  preset: 'glassMorph',
  lightColor: '#3498db',
  lightSize: 25,
  enableBurst: true,
  lightSizeEnterAnimationTime: 1000,
  lightSizeLeaveAnimationTime: 1000,
  mode: 'glow'
});

// Cleanup function
element.remove();

```

 --- 

## GlowHoverHookOptions

### Description


The `glowHoverEffect` function creates a glow effect on an element when hovered over.
### Parameters

#### el

##### Type


HTMLElement
##### Description


The target HTML element to apply the glow effect.

 --- 

#### options

##### Type


GlowHoverOptions
##### Description


An object containing configuration options for the glow effect.
### Return Value

#### void

##### Type


function()
##### Description


A function that cleans up the glow effect when called.
### Example Use
```ts 
// Example usage:
const cleanup = glowHoverEffect(someElement, {
  preset: 'presetName',
  lightColor: '#ff0000',
  hoverBg: 'rgba(255, 0, 0, 0.1)',
  enableBurst: true,
});
```
### Test Cases

#### Basic Usage Test

##### Description


Applies the glow effect with basic options and verifies cleanup function works.
##### Code
```ts 
// Setup
const el = document.createElement('div');
el.style.width = '100px';
el.style.height = '100px';

globalThis.document.body.appendChild(el);

// Apply effect
const cleanup = glowHoverEffect(el, {
  preset: 'basic',
  lightColor: '#ff0000'
});

// Test hover
el.dispatchEvent(new MouseEvent('mouseenter'));
expect(el.style.background).toContain('rgba(255, 0, 0, 0.1)');

// Cleanup and test
cleanup();
el.dispatchEvent(new MouseEvent('mouseleave'));
expect(el.style.background).toBe('');
globalThis.document.body.removeChild(el);
```

 --- 

## glowHoverEffect

### Description


Creates a glow hover effect on an HTML element. This function initializes the necessary animations and visual effects when the element is hovered over.
### Parameters

#### el

##### Type


HTMLElement
##### Description


The HTML element to which the glow effect will be applied.

 --- 

#### options

##### Type


GlowHoverOptions
##### Description


Configuration options for the glow hover effect.
### Return Value

#### 

##### Type


() => void
##### Description


A cleanup function that can be called to remove the glow effect from the element.
### Example Use
```ts 
const cleanup = glowHoverEffect(someElement, {
  preset: 'preset1',
  lightColor: '#ff0000'
});

// Later when you want to clean up
cleanup();
```
### Test Cases

#### Basic Usage

##### Description


Tests applying the glow effect with a basic configuration.
##### Code
```ts 
const el = document.createElement('div');
el.style.width = '100px';
el.style.height = '100px';

const cleanup = glowHoverEffect(el, {
  preset: 'preset1',
  lightColor: '#ff0000'
});

// Simulate hover
element.dispatchEvent(new MouseEvent('mouseenter'));

// Cleanup after test
cleanup();

```

 --- 

#### Custom Options

##### Description


Tests applying the glow effect with custom configuration options.
##### Code
```ts 
const el = document.createElement('div');
el.style.width = '100px';
el.style.height = '100px';

const cleanup = glowHoverEffect(el, {
  lightSize: 20,
  hoverBg: '#333',
  enableBurst: true,
  mode: 'sharp'
});

// Simulate hover
element.dispatchEvent(new MouseEvent('mouseenter'));

// Cleanup after test
cleanup();

```

 --- 

#### Force Theme

##### Description


Tests forcing a theme on hover using the forceTheme option.
##### Code
```ts 
const el = document.createElement('div');
el.style.width = '100px';
el.style.height = '100px';

const cleanup = glowHoverEffect(el, {
  forceTheme: 'dark'
});

// Simulate hover
element.dispatchEvent(new MouseEvent('mouseenter'));

// Cleanup after test
cleanup();

```

 --- 

## GlowHoverOptions

### Description


The GlowHoverEffect is a utility function that adds a glow hover effect to an HTML element. It allows customization through various options such as background color on hover, light size, animations, and more.
### Parameters

#### el

##### Type


HTMLElement
##### Description


The target HTML element where the glow hover effect will be applied.

 --- 

#### { preset, ...options }

##### Type


GlowHoverOptions
##### Description


An object containing various configuration options for the glow effect. The options include:
- `hoverBg`: String defining the background color on hover.
- `lightSize`: Number specifying the size of the light effect.
- `lightSizeEnterAnimationTime`: Number indicating the duration of the animation when entering the hover state.
- `lightSizeLeaveAnimationTime`: Number indicating the duration of the animation when leaving the hover state.
- `isElementMovable`: Boolean to determine if the element is movable during the effect.
- `customStaticBg`: String for a custom static background color.
- `forceTheme`: Enum ('light', 'dark', false) to force a specific theme on hover.
- `enableBurst`: Boolean to enable burst effects.
- `mode`: Enum ('glow', 'sharp') to choose between glow or sharp modes.

Additionally, the configuration can either specify a `preset` with optional `lightColor`, or provide explicit `lightColor` without using a preset.
### Return Value

#### () => void

##### Type


Function
##### Description


A cleanup function that can be called to remove the glow hover effect from the element.
### Example Use
```ts 

```
### Test Cases
