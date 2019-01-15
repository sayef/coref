import json
import sys
import util

def is_overlap(c1, c2):
  if c1[0] <= c2[0] and c2[0] <= c1[1]:
    return True
  return False

def count(data_file):
    f = open(data_file)
    max_num_sp = 0
    overlap, total = 0, 0
    for i, line in enumerate(f):
        # print('---', line)
        data = json.loads(line)
        clusters = util.flatten(data['clusters'])
        clusters = [tuple(c) for c in clusters]
        for c1 in clusters:
          for c2 in clusters:
            if c1 == c2:
              continue
            total += 1
            if (is_overlap(c1, c2)) or (is_overlap(c2, c1)):
              overlap += 1
              # print('overlap', c1, c2)
            # else:
              # print('non-overlap', c1, c2)
    print(overlap, total, overlap * 100.0 / total)

    print('max_num_sp', max_num_sp)

def avg_len(data_file):
    f = open(data_file)
    total = 0
    max_num_sp = 0
    segments = []
    limit = 250
    limit_exceeding = 0
    max_sent_len = 0
    sent_lens = []
    for i, line in enumerate(f):
        # print('---', line)
        data = json.loads(line)
        text = util.flatten(data['sentences'])
        segments.append(len(data['sentences']))
        total += len(text)
        long_sent = False
        for sentence in data['sentences']:
          max_sent_len = max(max_sent_len, len(sentence))
          sent_lens.append((data['doc_key'], len(sentence)))
          if len(sentence) > limit:
            long_sent = True
            print(sentence, data['doc_key'])
        limit_exceeding += int(long_sent)
        max_num_sp = max(max_num_sp, len(text))
    print(total / i)
    print(max_num_sp)
    print(len(segments), sum(segments) / len(segments), max(segments), sum([1 for s in segments if s == 1]))
    print('limit_exceeding/max', limit_exceeding, max_sent_len)
    print('topk', sorted(sent_lens, reverse=True, key=lambda s : s[1])[:20])

def cluster_distance(data_file):
    f = open(data_file)
    dist, pairs = 0, 0
    for i, line in enumerate(f):
        # print('---', line)
        data = json.loads(line)
        for cluster in data['clusters']:
            pairs += len(cluster) - 1
            spans = sorted([(s) for s,e in cluster])
            for i in range(len(spans) - 1):
                dist += spans[i+1] - spans[i]
    print(dist / pairs, pairs)


if __name__ == '__main__':
    data_file = sys.argv[1]
    avg_len(data_file)

