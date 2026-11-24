# One Word for Your Wi-Fi

[![make.fun](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/competitions/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/khususcrypto0000-coder/one-word-wifi-makefun/rank.svg)](https://make.fun/competitions/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/khususcrypto0000-coder/one-word-wifi-makefun/reward.svg)](https://make.fun/competitions/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

Entry for the make.fun bounty **One Word for Your Wi-Fi** — one word that
describes Wi-Fi, aiming to be both the funniest and the most accurate. The
winning word becomes the sponsor's Wi-Fi network name.

## The word

**cliffhanger**

Home Wi-Fi that always freezes right at the good part: the climax of the
episode, the boss's verdict on the video call, the final seconds of the
match. Full bars, then nothing — exactly when it matters most. Everyone
who has ever watched a loading spinner eat the best scene knows this
Wi-Fi by heart, and as a network name it is a joke every guest gets
the second they see it.

## Why this word

- **True:** the freeze always lands on the scene that matters, never on the ads.
- **Funny at once:** no explanation needed — the word itself is the punchline.
- **Fresh angle:** not another ghost, diva, or buffering joke; it names the
  timing of the failure, the part everyone actually curses at.
- **Works alone:** a common word, spelled the way everyone already spells it,
  and it reads perfectly as an SSID: `cliffhanger`.

## How it works

`main.py` (stdlib only) writes the word to `<OUTPUT_DIR>/entry.txt`
(default `/output/entry.txt`), with no trailing newline. It asserts the
gate before writing — 1–20 characters, a single word, not only
whitespace — then reads the file back and checks it is byte-identical.

```sh
python3 main.py
cat /output/entry.txt   # cliffhanger
```

## License

MIT — see [LICENSE](LICENSE).
