# Ideas

- Dusk
-

# .env

- Add addition .env keys to .env.example | .env.ci

# Nova

- Setup Nova

# Flare

```
'flare' => [
    'driver' => 'flare',
],

'stack' => [
    'driver' => 'stack',
    'channels' => ['daily', 'flare'],
    'ignore_exceptions' => false,
],
```

FLARE_KEY=