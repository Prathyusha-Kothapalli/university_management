import { useState, useEffect } from 'react';

/**
 * Hook that listens to viewport resize events and returns true when
 * the window width is at or below the given breakpoint (default 768px).
 * Automatically updates when the user resizes the browser or toggles
 * Chrome/Edge DevTools mobile inspection device toolbar.
 */
export const useIsMobile = (breakpoint = 768): boolean => {
  const [isMobile, setIsMobile] = useState<boolean>(() => {
    if (typeof window === 'undefined') return false;
    return window.innerWidth <= breakpoint;
  });

  useEffect(() => {
    if (typeof window === 'undefined') return;

    const checkMobile = () => {
      setIsMobile(window.innerWidth <= breakpoint);
    };

    // Initial check
    checkMobile();

    window.addEventListener('resize', checkMobile);
    window.addEventListener('orientationchange', checkMobile);

    return () => {
      window.removeEventListener('resize', checkMobile);
      window.removeEventListener('orientationchange', checkMobile);
    };
  }, [breakpoint]);

  return isMobile;
};

export default useIsMobile;
