
@rescui/use-glow-hover Documentation
====================================

## useGlowHover

### Description


A React hook that manages the hover effects with glowing animations for elements. It can automatically handle theme changes and provides various customization options through presets.
### Parameters

#### options

##### Type


GlowHoverHookOptions
##### Description


The options to customize the glow effect on hover.
### Return Value

#### refObject

##### Type


MutableRefObject<HTMLElement>
##### Description


A ref object that can be used to attach effects to elements in React components.
### Example Use
```ts 
const { memo } = React useMemoizedComparators; 
 const Box = () => {
   return (
     <div
       ref={useGlowHover({
         lightColor: '#FF6B6B',
         hoverBg: '#f0f0f0',
         enableBurst: true,
         mode: 'sharp'
       })}
     >
       Box with glow effect on hover
     </div>
   );
 };
```
### Test Cases

#### BasicUsage

##### Description


Tests the basic usage of the hook to ensure the glow effect is applied.
##### Code
```ts 
const container = document.createElement('div');
 const ref = useGlowHover({ lightColor: '#000', mode: 'glow' });
 ref.current = container;
 document.body.appendChild(container);
 // Test assertions here
```

 --- 

#### ThemeSwitching

##### Description


Tests the theme switching functionality when forceTheme is applied.
##### Code
```ts 
const container = document.createElement('div');
 const ref = useGlowHover({ forceTheme: 'dark' });
 ref.current = container;
 document.body.appendChild(container);
 // Test assertions here
```

 --- 

#### PresetUsage

##### Description


Tests the usage of a preset configuration.
##### Code
```ts 
const container = document.createElement('div');
 const ref = useGlowHover({ preset: 'default' });
 ref.current = container;
 document.body.appendChild(container);
 // Test assertions here
```

 --- 

#### BurstMode

##### Description


Tests the burst mode functionality.
##### Code
```ts 
const container = document.createElement('div');
 const ref = useGlowHover({ enableBurst: true });
 ref.current = container;
 document.body.appendChild(container);
 // Test assertions here
```

 --- 

## GlowHoverHookOptions

### Description


The `useGlowHover` hook provides a React Hook that adds an elegant hover effect with customizable glowing lights to elements. It supports both light and dark themes, theme forcing during hover, burst effects, and multiple customization options for size, timing, and more.
### Parameters

#### options

##### Type


GlowHoverHookOptions
##### Description


Options that customize the behavior of the glow effect on hover.
### Return Value

#### refObject

##### Type


MutableRefObject<HTMLElement>
##### Description


A mutable reference object that can be attached to a React component for the effect to apply.
### Example Use
```ts 
import { useGlowHover } from '@rescui/use-glow-hover';

function MyComponent() {
    const ref = useGlowHover({
        hoverBg: '#ff0000',
        lightSize: 15,
        lightSizeEnterAnimationTime: 200,
        lightSizeLeaveAnimationTime: 300,
        isElementMovable: true,
        customStaticBg: '#ffffff',
        forceTheme: 'dark',
        enableBurst: true,
        mode: 'glow'
    });

    return (
        <div ref={ref} className="my-class">
            Hover me!
        </div>
    );
}
```
### Test Cases

#### Basic Usage

##### Description


Tests the basic functionality of the hook with default options.
##### Code
```ts 
import { useGlowHover } from '@rescui/use-glow-hover';

const BasicTestCase = () => {
    const ref = useGlowHover();
    return (
        <div ref={ref} className="test-container">
            Hover me!
        </div>
    );
};
```

 --- 

#### Custom Theme

##### Description


Tests the ability to set a custom theme on hover.
##### Code
```ts 
import { useGlowHover } from '@rescui/use-glow-hover';

const CustomThemeTestCase = () => {
    const ref = useGlowHover({ forceTheme: 'dark' });
    return (
        <div ref={ref} className="test-container">
            Hover me with dark theme!
        </div>
    );
};
```

 --- 

#### Burst Effect

##### Description


Tests the burst effect functionality.
##### Code
```ts 
import { useGlowHover } from '@rescui/use-glow-hover';

const BurstTestCase = () => {
    const ref = useGlowHover({ enableBurst: true });
    return (
        <div ref={ref} className="test-container">
            Hover me to see the burst!
        </div>
    );
};
```

 --- 

#### Preset Usage

##### Description


Tests using a preset configuration for the glow effect.
##### Code
```ts 
import { useGlowHover } from '@rescui/use-glow-hover';

const PresetTestCase = () => {
    const ref = useGlowHover({
        preset: 'default'
    });
    return (
        <div ref={ref} className="test-container">
            Hover me with preset!
        </div>
    );
};
```

 --- 

#### Disabling the Effect

##### Description


Tests the functionality of disabling the hover effect.
##### Code
```ts 
import { useGlowHover } from '@rescui/use-glow-hover';

const DisabledTestCase = () => {
    const ref = useGlowHover({ disabled: true });
    return (
        <div ref={ref} className="test-container">
            This should not respond to hover!
        </div>
    );
};
```

 --- 

## glowHoverEffect

### Description


A React hook that adds a glow effect on hover to elements.
### Parameters

#### options

##### Type


GlowHoverOptions & { disabled?: boolean }
##### Description


The options for the glow effect.

 --- 

#### ref

##### Type


MutableRefObject<HTMLElement>
##### Description


A ref to the element to apply the glow effect to.
### Return Value

#### refWithGlowEffect

##### Type


MutableRefObject<HTMLElement>
##### Description


The ref with the glow effect applied.
### Example Use
```ts 
const ref = useGlowHover({
  preset: 'light',
  lightColor: '#ff0000'
}, elementRef);

```
### Test Cases

#### TestCase1

##### Description


Test case where glow effect is applied on hover.
##### Code
```ts 
const container = document.createElement('div');
container.style.width = '200px';
container.style.height = '200px';

const elementRef = ref;
useGlowHover({ preset: 'light', lightColor: '#ff0000' }, elementRef);

document.body.appendChild(container);

// Test if the glow effect is applied on hover
expect(getComputedStyle(container).getPropertyValue('box-shadow')).not.toBe('none');
```

 --- 

#### TestCase2

##### Description


Test case where no glow effect is applied when disabled.
##### Code
```ts 
const container = document.createElement('div');
container.style.width = '200px';
container.style.height = '200px';

const elementRef = ref;
useGlowHover({ preset: 'light', lightColor: '#ff0000', disabled: true }, elementRef);

document.body.appendChild(container);

// Test if the glow effect is not applied when disabled
expect(getComputedStyle(container).getPropertyValue('box-shadow')).toBe('none');
```

 --- 

## GlowHoverOptions

### Description


This is a React hook that adds a dynamic glow effect to elements on hover. It's useful for creating interactive UI components with smooth transitions.
### Parameters

#### options

##### Type


GlowHoverOptions | Partial<GlowHoverOptions>
##### Description


An object containing the configuration for the glow effect.
### Return Value

#### refObject

##### Type


MutableRefObject<HTMLElement>
##### Description


A React ref that can be used to attach the effect to a DOM element.
### Example Use
```ts 
function ExampleComponent() {
  const [mounted] = useMounted();
  const ref = useGlowHover({
    hoverBg: '#007bff',
    lightSize: 20,
    isElementMovable: true
  });

  useEffect(() => {
    if (mounted.current) {
      ref.current.style.color = '#ffffff';
    }
  }, [ref, mounted]);

  return (
    <button
      ref={ref}
      className="px-4 py-2 rounded-full bg-gray-800 text-white hover:bg-blue-500"
    >
      Hover me for glow effect!
    </button>
  );
}
```
### Test Cases

#### TestCase1

##### Description


Testing the basic usage of useGlowHover hook with minimal configuration.
##### Code
```ts 
import { render, screen } from '@testing-library/react';
import { useGlowHover } from '@rescui/use-glow-hover';

function TestCase1() {
  const ref = useGlowHover({ hoverBg: '#ff0000' });

  return (
    <div ref={ref} className="p-4 bg-gray-900 text-white">
      Hover over me to see the red glow effect.
    </div>
  );
}

describe('useGlowHover', () => {
  it('should render without crashing', () => {
    const { getByTestId } = render(<TestCase1 data-testid="test" />);
    expect(getByTestId('test')).toBeInTheDocument();
  });
});
```

 --- 

#### TestCase2

##### Description


Testing the effect when forceTheme is set to 'dark'.
##### Code
```ts 
import { render, screen } from '@testing-library/react';
import { useGlowHover } from '@rescui/use-glow-hover';

function TestCase2() {
  const ref = useGlowHover({ forceTheme: 'dark' });

  return (
    <div ref={ref} className="p-4 bg-gray-900 text-white">
      Hover over me to see the dark theme glow effect.
    </div>
  );
}

describe('useGlowHover', () => {
  it('should render without crashing', () => {
    const { getByTestId } = render(<TestCase2 data-testid="test" />);
    expect(getByTestId('test')).toBeInTheDocument();
  });
});
```

 --- 

#### TestCase3

##### Description


Testing the enableBurst option.
##### Code
```ts 
import { render, screen } from '@testing-library/react';
import { useGlowHover } from '@rescui/use-glow-hover';

function TestCase3() {
  const ref = useGlowHover({ enableBurst: true });

  return (
    <div ref={ref} className="p-4 bg-gray-900 text-white">
      Hover over me to see the burst glow effect.
    </div>
  );
}

describe('useGlowHover', () => {
  it('should render without crashing', () => {
    const { getByTestId } = render(<TestCase3 data-testid="test" />);
    expect(getByTestId('test')).toBeInTheDocument();
  });
});
```