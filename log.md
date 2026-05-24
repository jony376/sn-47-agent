2026-05-24 08:09:25 ✓ W&B initialized | Run:
2026-05-24 08:09:25 validator_5E9fVY1jexCNVMjd2rdBsAxeamFGEMfzHcyTn2fHgdHeYc5p_20260524_080924
2026-05-24 08:09:25 
2026-05-24 08:09:25 Loading reference tokenizer: Qwen/Qwen3.5-9B…
2026-05-24 08:09:26 ✓ Reference tokenizer loaded (vocab_size=248044)
2026-05-24 08:09:26 Starting ref vLLM server (Qwen/Qwen3.5-9B) on port 8002…
2026-05-24 08:09:26 08:09:26 [evolai.validator.vllm_client] INFO: Starting vLLM server for Qwen/Qwen3.5-9B@main on port 8002 (CUDA device=0, tp=1)
2026-05-24 08:09:26 08:09:26 [evolai.validator.vllm_client] INFO: vLLM stdout → /tmp/vllm_server_8002.log  (tail -f /tmp/vllm_server_8002.log)
2026-05-24 08:09:26 08:09:26 [evolai.validator.vllm_client] INFO: vLLM cmd: /root/.bittensor/subnets/evolai/vllm_env/bin/vllm serve Qwen/Qwen3.5-9B --host 127.0.0.1 --port 8002 --revision main --dtype bfloat16 --gpu-memory-utilization 0.5 --max-model-len 4096 --tensor-parallel-size 1 --served-model-name Qwen/Qwen3.5-9B --no-enable-prefix-caching
2026-05-24 08:09:26 08:09:26 [evolai.validator.vllm_client] INFO: Waiting for vLLM server to be ready (max 600.0s)...
2026-05-24 08:09:41 08:09:41 [evolai.validator.vllm_client] INFO:   Still waiting for vLLM server... (15s elapsed)
2026-05-24 08:09:56 08:09:56 [evolai.validator.vllm_client] INFO:   Still waiting for vLLM server... (30s elapsed)
2026-05-24 08:10:11 08:10:11 [evolai.validator.vllm_client] INFO:   Still waiting for vLLM server... (45s elapsed)
2026-05-24 08:10:26 08:10:26 [evolai.validator.vllm_client] INFO:   Still waiting for vLLM server... (60s elapsed)
2026-05-24 08:10:41 08:10:41 [evolai.validator.vllm_client] INFO:   Still waiting for vLLM server... (75s elapsed)
2026-05-24 08:10:56 08:10:56 [evolai.validator.vllm_client] INFO:   Still waiting for vLLM server... (90s elapsed)
2026-05-24 08:11:11 08:11:11 [evolai.validator.vllm_client] INFO:   Still waiting for vLLM server... (105s elapsed)
2026-05-24 08:11:26 08:11:26 [evolai.validator.vllm_client] INFO:   Still waiting for vLLM server... (120s elapsed)
2026-05-24 08:11:41 08:11:41 [evolai.validator.vllm_client] INFO:   Still waiting for vLLM server... (135s elapsed)
2026-05-24 08:11:56 08:11:56 [evolai.validator.vllm_client] INFO:   Still waiting for vLLM server... (150s elapsed)
2026-05-24 08:12:11 08:12:11 [evolai.validator.vllm_client] INFO:   Still waiting for vLLM server... (165s elapsed)
2026-05-24 08:12:26 08:12:26 [evolai.validator.vllm_client] INFO:   Still waiting for vLLM server... (180s elapsed)
2026-05-24 08:12:29 08:12:29 [evolai.validator.vllm_client] INFO: vLLM server ready at http://127.0.0.1:8002/v1 (183s)
2026-05-24 08:12:29 ✓ Ref vLLM server running at http://127.0.0.1:8002/v1
2026-05-24 08:12:30 
2026-05-24 08:12:30 ╭─────────────────────── Starting Validator Loop ────────────────────────╮
2026-05-24 08:12:30 │ Validator Configuration                                                │
2026-05-24 08:12:30 │                                                                        │
2026-05-24 08:12:30 │ Netuid: 47                                                             │
2026-05-24 08:12:30 │ Tracks: transformer, mamba2                                            │
2026-05-24 08:12:30 │ Eval Mode: Continuous round-seeded decentralised                       │
2026-05-24 08:12:30 │ Epoch Blocks: 360 (~72 min/chain epoch)                                │
2026-05-24 08:12:30 │ Eval rows per dataset: transformer=20, mamba2=20                       │
2026-05-24 08:12:30 │ Fast transformer: True (flat_turns=True, skip_ce=False, skip_sq=False) │
2026-05-24 08:12:30 │ Active datasets: evolai/universal_qa                                   │
2026-05-24 08:12:30 │ Score weights: abs=0.6 flow=0.3 sq=0.1                                 │
2026-05-24 08:12:30 │ Quality gates: improve=True consistency=True next/current≤1.20         │
2026-05-24 08:12:30 │ EMA alpha: 0.1  Min flow epochs: 10  Emission λ: 0.1                   │
2026-05-24 08:12:30 │ History epochs: 1800                                                   │
2026-05-24 08:12:30 │ W&B Logging: True                                                      │
2026-05-24 08:12:30 │ W&B Project: evol-validator                                            │
2026-05-24 08:12:30 │ Owner API (telemetry only): https://evolai-gate.hf.space               │
2026-05-24 08:12:30 ╰────────────────────────────────────────────────────────────────────────╯
2026-05-24 08:12:30 
2026-05-24 08:12:30 Start continuous evaluation loop? [y/n]:
2026-05-24 08:12:30 Validator loop started (Press Ctrl+C to stop)
2026-05-24 08:12:30 
2026-05-24 08:12:30 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2026-05-24 08:12:30 
2026-05-24 08:12:30 ━━━ Epoch #22924 (Loop #1) ━━━ block=8252673, ~65m remaining
2026-05-24 08:12:36 
2026-05-24 08:12:36   Using seed from validator UID 4 (epoch 22923)
2026-05-24 08:12:46   ⚠ UID 86: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:12:46 (Request ID:
2026-05-24 08:12:46 Root=1-6a12b2fe-500d79e74be9f4805cefa530;6cbe02bd-9da4-4d8e-9807-a1a9225a4ea8)
2026-05-24 08:12:46 
2026-05-24 08:12:46 Repository Not Found for url:
2026-05-24 08:12:46 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-012/revision/main.
2026-05-24 08:12:46 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:12:46 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:12:46 authenticated and your token has the required permissions.
2026-05-24 08:12:46 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:12:46 Invalid username or password.
2026-05-24 08:12:46   ⚠ UID 87: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:12:46 (Request ID:
2026-05-24 08:12:46 Root=1-6a12b2fe-1d8d307177b773c37bd9fd6e;bd23a4db-6658-4f1d-b9f5-3646b9c5ab11)
2026-05-24 08:12:46 
2026-05-24 08:12:46 Repository Not Found for url:
2026-05-24 08:12:46 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-013/revision/main.
2026-05-24 08:12:46 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:12:46 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:12:46 authenticated and your token has the required permissions.
2026-05-24 08:12:46 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:12:46 Invalid username or password.
2026-05-24 08:12:46   ⚠ UID 88: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:12:46 (Request ID:
2026-05-24 08:12:46 Root=1-6a12b2fe-0302ae027d76a3bf24cf427b;61ad86aa-1ae0-47df-b721-77efd2c44a23)
2026-05-24 08:12:46 
2026-05-24 08:12:46 Repository Not Found for url:
2026-05-24 08:12:46 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-014/revision/main.
2026-05-24 08:12:46 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:12:46 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:12:46 authenticated and your token has the required permissions.
2026-05-24 08:12:46 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:12:46 Invalid username or password.
2026-05-24 08:12:47   Locked transformer revisions (50 miner(s), 3 skipped)
2026-05-24 08:12:54   ⚠ UID 63: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:12:54 (Request ID:
2026-05-24 08:12:54 Root=1-6a12b306-674c7d386ce57a8b2174b953;30874abd-2dab-4fe1-b973-958c64e6b652)
2026-05-24 08:12:54 
2026-05-24 08:12:54 Repository Not Found for url:
2026-05-24 08:12:54 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-009/revision/main.
2026-05-24 08:12:54 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:12:54 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:12:54 authenticated and your token has the required permissions.
2026-05-24 08:12:54 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:12:54 Invalid username or password.
2026-05-24 08:12:54   ⚠ UID 64: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:12:54 (Request ID:
2026-05-24 08:12:54 Root=1-6a12b306-54c9725b779ef04601cf9f0f;8a401921-931f-4a86-918e-8b1cfe54c83b)
2026-05-24 08:12:54 
2026-05-24 08:12:54 Repository Not Found for url:
2026-05-24 08:12:54 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-002/revision/main.
2026-05-24 08:12:54 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:12:54 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:12:54 authenticated and your token has the required permissions.
2026-05-24 08:12:54 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:12:54 Invalid username or password.
2026-05-24 08:12:54   ⚠ UID 68: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:12:54 (Request ID:
2026-05-24 08:12:54 Root=1-6a12b306-20ca26662706fcd920c07566;0be9da23-719f-403b-87e5-2ff731da983f)
2026-05-24 08:12:54 
2026-05-24 08:12:54 Repository Not Found for url:
2026-05-24 08:12:54 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-008/revision/main.
2026-05-24 08:12:54 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:12:54 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:12:54 authenticated and your token has the required permissions.
2026-05-24 08:12:54 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:12:54 Invalid username or password.
2026-05-24 08:12:54   ⚠ UID 71: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:12:54 (Request ID:
2026-05-24 08:12:54 Root=1-6a12b306-5b4069777c61a7227fba5124;17e88a47-170e-424f-818a-2a2d805bada8)
2026-05-24 08:12:54 
2026-05-24 08:12:54 Repository Not Found for url:
2026-05-24 08:12:54 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-001/revision/main.
2026-05-24 08:12:54 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:12:54 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:12:54 authenticated and your token has the required permissions.
2026-05-24 08:12:54 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:12:54 Invalid username or password.
2026-05-24 08:12:55   ⚠ UID 74: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:12:55 (Request ID:
2026-05-24 08:12:55 Root=1-6a12b306-666101cb7849b0033957e38f;5331610e-42ed-47ea-886b-ee299efcf1d8)
2026-05-24 08:12:55 
2026-05-24 08:12:55 Repository Not Found for url:
2026-05-24 08:12:55 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-007/revision/main.
2026-05-24 08:12:55 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:12:55 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:12:55 authenticated and your token has the required permissions.
2026-05-24 08:12:55 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:12:55 Invalid username or password.
2026-05-24 08:12:55   ⚠ UID 81: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:12:55 (Request ID:
2026-05-24 08:12:55 Root=1-6a12b307-718fc42238bad4a33d2040c6;52a7c7fd-a772-44d1-a9b9-72dab00c9056)
2026-05-24 08:12:55 
2026-05-24 08:12:55 Repository Not Found for url:
2026-05-24 08:12:55 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-010/revision/main.
2026-05-24 08:12:55 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:12:55 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:12:55 authenticated and your token has the required permissions.
2026-05-24 08:12:55 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:12:55 Invalid username or password.
2026-05-24 08:12:55   Locked mamba2 revisions (15 miner(s), 6 skipped)
2026-05-24 08:13:26   Committed round seed epoch=22924 seed=d05a5edc...
2026-05-24 08:13:27 Evaluating TRANSFORMER track…
2026-05-24 08:13:27 
2026-05-24 08:13:27   Found 50 locked transformer miners
2026-05-24 08:13:27 Pre-building current/next challenges for 50 miners…
2026-05-24 08:13:27    Downloading
2026-05-24 08:13:27 andrebarrosilva1123/evolai-b@3414c0abb8793ed4af56fd5e6e536b8b0f5ac520…
2026-05-24 08:13:27 Fetching 7 files: 100%|██████████| 7/7 [00:06<00:00,  1.06it/s]
2026-05-24 08:13:31    alpha=0.005511 TAO/α  budget=0.049177
2026-05-24 08:13:33    Ready: andrebarrosilva1123/evolai-b@3414c0abb8793ed4af56fd5e6e536b8b0f5ac520
2026-05-24 08:13:33    Downloading
2026-05-24 08:13:33 logosnodos/evolai-qwen-1.5b@7e121e8efe6c6b93d622e9a53972d221e763d10b…
2026-05-24 08:13:34 Fetching 17 files: 100%|██████████| 17/17 [00:56<00:00,  3.35s/it]
2026-05-24 08:14:08    emission scale=1.000 (active miners)
2026-05-24 08:14:08    emission scale=1.000 (active miners)
2026-05-24 08:14:08    all quality scores zero after gates — emission share redistributed to
2026-05-24 08:14:08 productive tracks
2026-05-24 08:14:09   ✓  set at 08:14:09 UTC
2026-05-24 08:14:31    Ready: logosnodos/evolai-qwen-1.5b@7e121e8efe6c6b93d622e9a53972d221e763d10b
2026-05-24 08:15:24 ✓ Ref data ready: submitted=100, cached=0
2026-05-24 08:15:24   [1/50] UID 50 | andrebarrosilva1123/evolai-b @
2026-05-24 08:15:24 3414c0abb8793ed4af56fd5e6e536b8b0f5ac520 | hotkey 5FXELcBK4WiD…
2026-05-24 08:15:24     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:15:24     Fetched 20 texts (20 indices)
2026-05-24 08:15:24    Downloading
2026-05-24 08:15:24 andrebarrosilva1123/evolai-0.4b@fa913c93aa7a7449066ce870427387bd3fc7e841…
2026-05-24 08:15:24 Fetching 7 files: 100%|██████████| 7/7 [00:07<00:00,  1.00s/it]
2026-05-24 08:15:29     Loaded (local prefetch)
2026-05-24 08:15:30     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:15:31    Ready:
2026-05-24 08:15:31 andrebarrosilva1123/evolai-0.4b@fa913c93aa7a7449066ce870427387bd3fc7e841
2026-05-24 08:15:32   [2/50] UID 61 | logosnodos/evolai-qwen-1.5b @
2026-05-24 08:15:32 7e121e8efe6c6b93d622e9a53972d221e763d10b | hotkey 5FNTU6ZYgKup…
2026-05-24 08:15:32     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:15:32    Downloading
2026-05-24 08:15:32 mrthor102/evolai-tfm-super-003@81700a3fcf9c5db81d016022dfcb41ba57ff1801…
2026-05-24 08:15:32     Fetched 20 texts (20 indices)
2026-05-24 08:15:36     Loaded (local prefetch)
2026-05-24 08:15:39    Ready:
2026-05-24 08:15:39 mrthor102/evolai-tfm-super-003@81700a3fcf9c5db81d016022dfcb41ba57ff1801
2026-05-24 08:15:41     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:15:42   [3/50] UID 49 | andrebarrosilva1123/evolai-0.4b @
2026-05-24 08:15:42 fa913c93aa7a7449066ce870427387bd3fc7e841 | hotkey 5DULz3AJEisH…
2026-05-24 08:15:42     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:15:42     Fetched 20 texts (20 indices)
2026-05-24 08:15:42    Downloading
2026-05-24 08:15:42 clear-blue-sky/evolai-reborn-tfm-011@ad7a4cffc147267f7c81848b5c5ebdfb3ede9818…
2026-05-24 08:15:44     Loaded (local prefetch)
2026-05-24 08:15:45     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:15:47   [4/50] UID 98 | mrthor102/evolai-tfm-super-003 @
2026-05-24 08:15:47 81700a3fcf9c5db81d016022dfcb41ba57ff1801 | hotkey 5Hgy59m2Hzm1…
2026-05-24 08:15:47     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:15:47     Fetched 20 texts (20 indices)
2026-05-24 08:15:47    Ready:
2026-05-24 08:15:47 clear-blue-sky/evolai-reborn-tfm-011@ad7a4cffc147267f7c81848b5c5ebdfb3ede9818
2026-05-24 08:15:47    Downloading
2026-05-24 08:15:47 Radiant28/evolai-transformer-0.4b-b2@808b61992e043ca99ff5b412a6cf61bfbb3fd793…
2026-05-24 08:15:50     Loaded (local prefetch)
2026-05-24 08:15:50     Model 0.46B → batch=512, seq=16384
2026-05-24 08:15:53    Ready:
2026-05-24 08:15:53 Radiant28/evolai-transformer-0.4b-b2@808b61992e043ca99ff5b412a6cf61bfbb3fd793
2026-05-24 08:19:16     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:56
2026-05-24 08:19:16     Loss 3.8961 | Size ×0.50 | Think 3.8961 | ThinkGain 0 (+0.4591) | Flow
2026-05-24 08:19:16 0.1390 | KL 2.0310 | NextKL 2.0076 | SideQ 0% | Score 0.0000 (205.9s)
2026-05-24 08:19:16     Gate FAIL | Improve seed/ref mismatch cur=2.0310 req<=0.0000 prev=mismatch |
2026-05-24 08:19:16 Consist ok ema_cur=1.9060 ema_next=1.9134 ratio=1.004 max<=1.20
2026-05-24 08:19:17   [5/50] UID 73 | clear-blue-sky/evolai-reborn-tfm-011 @
2026-05-24 08:19:17 ad7a4cffc147267f7c81848b5c5ebdfb3ede9818 | hotkey 5CSAM6rnGRPk…
2026-05-24 08:19:17     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:19:17     Fetched 20 texts (20 indices)
2026-05-24 08:19:17    Downloading
2026-05-24 08:19:17 mrthor102/evolai-tfm-super-002@71e1421aeba07a1a80e1455d15564e1efcd2b72b…
2026-05-24 08:19:20     Loaded (local prefetch)
2026-05-24 08:19:21     Model 0.46B → batch=512, seq=16384
2026-05-24 08:19:22    Ready:
2026-05-24 08:19:22 mrthor102/evolai-tfm-super-002@71e1421aeba07a1a80e1455d15564e1efcd2b72b
2026-05-24 08:20:15     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:51
2026-05-24 08:20:16     Loss 3.8153 | Size ×0.50 | Think 3.8153 | ThinkGain 0 (+0.4631) | Flow
2026-05-24 08:20:16 0.0000 | KL 1.8722 | NextKL 1.8450 | SideQ 0% | Score 0.0000 (54.8s)
2026-05-24 08:20:16     Gate FAIL | Improve seed/ref mismatch cur=1.8722 req<=0.0000 prev=mismatch |
2026-05-24 08:20:16 Consist ok ema_cur=2.5893 ema_next=1.8613 ratio=0.719 max<=1.20
2026-05-24 08:20:17   [6/50] UID 37 | Radiant28/evolai-transformer-0.4b-b2 @
2026-05-24 08:20:17 808b61992e043ca99ff5b412a6cf61bfbb3fd793 | hotkey 5HjbzF3e9waA…
2026-05-24 08:20:17     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:20:17    Downloading
2026-05-24 08:20:17 mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c…
2026-05-24 08:20:17     Fetched 20 texts (20 indices)
2026-05-24 08:20:19     Loaded (local prefetch)
2026-05-24 08:20:20     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:20:20    Ready: mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c
2026-05-24 08:20:22   [7/50] UID 97 | mrthor102/evolai-tfm-super-002 @
2026-05-24 08:20:22 71e1421aeba07a1a80e1455d15564e1efcd2b72b | hotkey 5EcJYRJBVF5K…
2026-05-24 08:20:22     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:20:22     Fetched 20 texts (20 indices)
2026-05-24 08:20:22    Downloading
2026-05-24 08:20:22 mrthor102/evolai-tfm-super-001@f7d9445d9182dd4333dbe32ebd6a7853649a8f41…
2026-05-24 08:20:25     Loaded (local prefetch)
2026-05-24 08:20:25     Model 0.46B → batch=512, seq=16384
2026-05-24 08:20:27    Ready:
2026-05-24 08:20:27 mrthor102/evolai-tfm-super-001@f7d9445d9182dd4333dbe32ebd6a7853649a8f41
2026-05-24 08:21:24     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:56
2026-05-24 08:21:25     Loss 3.9830 | Size ×0.50 | Think 3.9830 | ThinkGain 0 (+0.4636) | Flow
2026-05-24 08:21:25 0.0000 | KL 1.8816 | NextKL 1.9169 | SideQ 0% | Score 0.0000 (59.2s)
2026-05-24 08:21:25     Gate FAIL | Improve seed/ref mismatch cur=1.8816 req<=0.0000 prev=mismatch |
2026-05-24 08:21:25 Consist ok ema_cur=1.9320 ema_next=1.9280 ratio=0.998 max<=1.20
2026-05-24 08:21:26   [8/50] UID 33 | mihai-777/evolai-tfm-1p5b @
2026-05-24 08:21:26 594894f806fb4c014675d89aad14f1c68976d52c | hotkey 5F22JM4of6TR…
2026-05-24 08:21:26     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:21:26     Fetched 20 texts (20 indices)
2026-05-24 08:21:26    Downloading snx999/evolai_qw_4b@69eff663b4e9a2b5bf76dde6cdecc5dce29759d3…
2026-05-24 08:21:27     Loaded (local prefetch)
2026-05-24 08:21:27     Model 0.46B → batch=512, seq=16384
2026-05-24 08:21:41    Ready: snx999/evolai_qw_4b@69eff663b4e9a2b5bf76dde6cdecc5dce29759d3
2026-05-24 08:22:30     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:59
2026-05-24 08:22:30     Loss 2.8796 | Size ×0.50 | Think 2.8796 | ThinkGain 0 (+0.4519) | Flow
2026-05-24 08:22:30 0.0420 | KL 2.2918 | NextKL 2.5351 | SideQ 0% | Score 0.0000 (62.3s)
2026-05-24 08:22:30     Gate FAIL | Improve seed/ref mismatch cur=2.2918 req<=0.0000 prev=mismatch |
2026-05-24 08:22:30 Consist ok ema_cur=2.4013 ema_next=2.4350 ratio=1.014 max<=1.20
2026-05-24 08:22:31   [9/50] UID 94 | mrthor102/evolai-tfm-super-001 @
2026-05-24 08:22:31 f7d9445d9182dd4333dbe32ebd6a7853649a8f41 | hotkey 5CPXihPMoGQ2…
2026-05-24 08:22:31     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:22:31     Fetched 20 texts (20 indices)
2026-05-24 08:22:31    Downloading
2026-05-24 08:22:31 Radiant28/evolai-transformer-0.4b-b0@7a08a8009fa8b8f82d1ad0febc442a89020082d1…
2026-05-24 08:22:33     Loaded (local prefetch)
2026-05-24 08:22:33     Model 0.46B → batch=512, seq=16384
2026-05-24 08:22:37    Ready:
2026-05-24 08:22:37 Radiant28/evolai-transformer-0.4b-b0@7a08a8009fa8b8f82d1ad0febc442a89020082d1
2026-05-24 08:23:33     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:55
2026-05-24 08:23:33     Loss 3.7989 | Size ×0.50 | Think 3.7989 | ThinkGain 0 (+0.4579) | Flow
2026-05-24 08:23:33 0.0000 | KL 1.7722 | NextKL 1.9535 | SideQ 0% | Score 0.0000 (59.6s)
2026-05-24 08:23:33     Gate FAIL | Improve seed/ref mismatch cur=1.7722 req<=0.0000 prev=mismatch |
2026-05-24 08:23:33 Consist ok ema_cur=1.9267 ema_next=1.9433 ratio=1.009 max<=1.20
2026-05-24 08:23:34   [10/50] UID 25 | snx999/evolai_qw_4b @
2026-05-24 08:23:34 69eff663b4e9a2b5bf76dde6cdecc5dce29759d3 | hotkey 5HBJoNWv4nAi…
2026-05-24 08:23:34     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:23:34    Downloading
2026-05-24 08:23:34 clear-blue-sky/evolai-reborn-tfm-002@3c1af863d3a626ef7f225f335e95f12a17870386…
2026-05-24 08:23:34     Fetched 20 texts (20 indices)
2026-05-24 08:23:39    Ready:
2026-05-24 08:23:39 clear-blue-sky/evolai-reborn-tfm-002@3c1af863d3a626ef7f225f335e95f12a17870386
2026-05-24 08:23:39     Loaded (local prefetch)
2026-05-24 08:23:40     ⚠ Invalid model size (4.21B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 08:23:42   [11/50] UID 45 | Radiant28/evolai-transformer-0.4b-b0 @
2026-05-24 08:23:42 7a08a8009fa8b8f82d1ad0febc442a89020082d1 | hotkey 5F1B3j7EyjuE…
2026-05-24 08:23:42     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:23:42     Fetched 20 texts (20 indices)
2026-05-24 08:23:42    Downloading
2026-05-24 08:23:42 clear-blue-sky/evolai-reborn-tfm-010@29651f934f3b275247eaca45fd35518d83e94a0d…
2026-05-24 08:23:44     Loaded (local prefetch)
2026-05-24 08:23:45     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:23:46    Ready:
2026-05-24 08:23:46 clear-blue-sky/evolai-reborn-tfm-010@29651f934f3b275247eaca45fd35518d83e94a0d
2026-05-24 08:23:47   [12/50] UID 67 | clear-blue-sky/evolai-reborn-tfm-002 @
2026-05-24 08:23:47 3c1af863d3a626ef7f225f335e95f12a17870386 | hotkey 5GC7k2mkTKGF…
2026-05-24 08:23:47     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:23:47     Fetched 20 texts (20 indices)
2026-05-24 08:23:47    Downloading
2026-05-24 08:23:47 mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678…
2026-05-24 08:23:50     Loaded (local prefetch)
2026-05-24 08:23:50     Model 0.46B → batch=512, seq=16384
2026-05-24 08:23:50    Ready: mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678
2026-05-24 08:24:49     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:56
2026-05-24 08:24:50     Loss 3.6892 | Size ×0.50 | Think 3.6892 | ThinkGain 0 (+0.4584) | Flow
2026-05-24 08:24:50 0.4569 | KL 1.8500 | NextKL 1.9166 | SideQ 0% | Score 0.0000 (59.6s)
2026-05-24 08:24:50     Gate FAIL | Improve seed/ref mismatch cur=1.8500 req<=0.0000 prev=mismatch |
2026-05-24 08:24:50 Consist ok ema_cur=1.8913 ema_next=1.8944 ratio=1.002 max<=1.20
2026-05-24 08:24:50   [13/50] UID 72 | clear-blue-sky/evolai-reborn-tfm-010 @
2026-05-24 08:24:50 29651f934f3b275247eaca45fd35518d83e94a0d | hotkey 5H3rMcqJQcbK…
2026-05-24 08:24:50     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:24:50     Fetched 20 texts (20 indices)
2026-05-24 08:24:50    Downloading
2026-05-24 08:24:50 mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a…
2026-05-24 08:24:52     Loaded (local prefetch)
2026-05-24 08:24:52     Model 0.46B → batch=512, seq=16384
2026-05-24 08:24:54    Ready: mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a
2026-05-24 08:25:52     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:56
2026-05-24 08:25:53     Loss 3.5856 | Size ×0.50 | Think 3.5856 | ThinkGain 0 (+0.4598) | Flow
2026-05-24 08:25:53 0.0000 | KL 1.9312 | NextKL 1.6153 | SideQ 0% | Score 0.0000 (60.0s)
2026-05-24 08:25:53     Gate FAIL | Improve seed/ref mismatch cur=1.9312 req<=0.0000 prev=mismatch |
2026-05-24 08:25:53 Consist ok ema_cur=1.9073 ema_next=1.8996 ratio=0.996 max<=1.20
2026-05-24 08:25:54   [14/50] UID 42 | mihai-777/evolai-tfm-1p5b-v5 @
2026-05-24 08:25:54 bd42aeb0828dfa0126f7fc825e13b49209fec678 | hotkey 5C5WCYnsrXRz…
2026-05-24 08:25:54     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:25:54     Fetched 20 texts (20 indices)
2026-05-24 08:25:54    Downloading
2026-05-24 08:25:54 andrebarrosilva1123/evolai-e@806394ca7f2f7c1edbe962a9471647f4d67b5e72…
2026-05-24 08:25:55     Loaded (local prefetch)
2026-05-24 08:25:56     Model 0.46B → batch=512, seq=16384
2026-05-24 08:26:01    Ready: andrebarrosilva1123/evolai-e@806394ca7f2f7c1edbe962a9471647f4d67b5e72
2026-05-24 08:26:30     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:32
2026-05-24 08:26:30     Loss 2.9319 | Size ×0.50 | Think 2.9319 | ThinkGain 0 (+0.4562) | Flow
2026-05-24 08:26:30 0.1891 | KL 2.4191 | NextKL 2.4519 | SideQ 0% | Score 0.0000 (34.3s)
2026-05-24 08:26:30     Gate FAIL | Improve seed/ref mismatch cur=2.4191 req<=0.0000 prev=mismatch |
2026-05-24 08:26:30 Consist ok ema_cur=2.4356 ema_next=2.4515 ratio=1.007 max<=1.20
2026-05-24 08:26:31   Evicted cached model:
2026-05-24 08:26:31 mrthor102/evolai-tfm-super-003@81700a3fcf9c5db81d016022dfcb41ba57ff1801
2026-05-24 08:26:32   [15/50] UID 75 | mihai-777/evolai-tfm-1p5b-04 @
2026-05-24 08:26:32 fb289dbfe35c595b1a586f786a19e118cc1bfc9a | hotkey 5Dnz76SAsEv8…
2026-05-24 08:26:32     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:26:32     Fetched 20 texts (20 indices)
2026-05-24 08:26:32    Downloading
2026-05-24 08:26:32 clear-blue-sky/evolai-reborn-tfm-006@27bbbdbe12605a00573f2af96d1d99d61e430ce6…
2026-05-24 08:26:33     Loaded (local prefetch)
2026-05-24 08:26:33     Model 0.46B → batch=512, seq=16384
2026-05-24 08:26:36    Ready:
2026-05-24 08:26:36 clear-blue-sky/evolai-reborn-tfm-006@27bbbdbe12605a00573f2af96d1d99d61e430ce6
2026-05-24 08:27:09     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:33
2026-05-24 08:27:09     Loss 2.9821 | Size ×0.50 | Think 2.9821 | ThinkGain 0 (+0.4494) | Flow
2026-05-24 08:27:09 0.2608 | KL 2.2377 | NextKL 2.2630 | SideQ 0% | Score 0.0000 (35.5s)
2026-05-24 08:27:09     Gate FAIL | Improve seed/ref mismatch cur=2.2377 req<=0.0000 prev=mismatch |
2026-05-24 08:27:09 Consist ok ema_cur=2.3413 ema_next=2.3526 ratio=1.005 max<=1.20
2026-05-24 08:27:11   Evicted cached model:
2026-05-24 08:27:11 clear-blue-sky/evolai-reborn-tfm-011@ad7a4cffc147267f7c81848b5c5ebdfb3ede9818
2026-05-24 08:27:11   [16/50] UID 53 | andrebarrosilva1123/evolai-e @
2026-05-24 08:27:11 806394ca7f2f7c1edbe962a9471647f4d67b5e72 | hotkey 5EFgFa93M5Vx…
2026-05-24 08:27:11     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:27:11     Fetched 20 texts (20 indices)
2026-05-24 08:27:11    Downloading
2026-05-24 08:27:11 Radiant28/evolai-transformer-0.4b-b1@18231d7d50096d8b2744fdff1b38a7b90246ddf0…
2026-05-24 08:27:13     Loaded (local prefetch)
2026-05-24 08:27:13     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:27:15   [17/50] UID 66 | clear-blue-sky/evolai-reborn-tfm-006 @
2026-05-24 08:27:15 27bbbdbe12605a00573f2af96d1d99d61e430ce6 | hotkey 5E4M4B5sVED5…
2026-05-24 08:27:15     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:27:15     Fetched 20 texts (20 indices)
2026-05-24 08:27:17     Loaded (local prefetch)
2026-05-24 08:27:17     Model 0.46B → batch=512, seq=16384
2026-05-24 08:27:17    Ready:
2026-05-24 08:27:17 Radiant28/evolai-transformer-0.4b-b1@18231d7d50096d8b2744fdff1b38a7b90246ddf0
2026-05-24 08:27:17    Downloading
2026-05-24 08:27:17 clear-blue-sky/evolai-reborn-tfm-007@ba9045012f93d80b69da2201376756708f45f355…
2026-05-24 08:27:17 Fetching 7 files: 100%|██████████| 7/7 [00:04<00:00,  1.70it/s]
2026-05-24 08:27:22    Ready:
2026-05-24 08:27:22 clear-blue-sky/evolai-reborn-tfm-007@ba9045012f93d80b69da2201376756708f45f355
2026-05-24 08:27:54     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 08:27:54     Loss 3.9005 | Size ×0.50 | Think 3.9005 | ThinkGain 0 (+0.4594) | Flow
2026-05-24 08:27:54 0.0000 | KL 2.0171 | NextKL 1.9499 | SideQ 0% | Score 0.0000 (36.8s)
2026-05-24 08:27:54     Gate FAIL | Improve seed/ref mismatch cur=2.0171 req<=0.0000 prev=mismatch |
2026-05-24 08:27:54 Consist ok ema_cur=1.9693 ema_next=1.9609 ratio=0.996 max<=1.20
2026-05-24 08:27:56   Evicted cached model:
2026-05-24 08:27:56 mrthor102/evolai-tfm-super-002@71e1421aeba07a1a80e1455d15564e1efcd2b72b
2026-05-24 08:27:56   [18/50] UID 35 | Radiant28/evolai-transformer-0.4b-b1 @
2026-05-24 08:27:56 18231d7d50096d8b2744fdff1b38a7b90246ddf0 | hotkey 5EXZBq3wQzTK…
2026-05-24 08:27:56    Downloading Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600…
2026-05-24 08:27:56     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:27:56     Fetched 20 texts (20 indices)
2026-05-24 08:27:58     Loaded (local prefetch)
2026-05-24 08:27:58    Ready: Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600
2026-05-24 08:27:59     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:28:00   [19/50] UID 84 | clear-blue-sky/evolai-reborn-tfm-007 @
2026-05-24 08:28:00 ba9045012f93d80b69da2201376756708f45f355 | hotkey 5H1DaT8Dtt4N…
2026-05-24 08:28:00     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:28:00    Downloading
2026-05-24 08:28:00 clear-blue-sky/evolai-reborn-tfm-003@db37ac46734d13b9f00d6049d02ad79254bcd03f…
2026-05-24 08:28:00     Fetched 20 texts (20 indices)
2026-05-24 08:28:02     Loaded (local prefetch)
2026-05-24 08:28:02     Model 0.46B → batch=512, seq=16384
2026-05-24 08:28:04    Ready:
2026-05-24 08:28:04 clear-blue-sky/evolai-reborn-tfm-003@db37ac46734d13b9f00d6049d02ad79254bcd03f
2026-05-24 08:28:37     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:33
2026-05-24 08:28:38     Loss 3.7714 | Size ×0.50 | Think 3.7714 | ThinkGain 0 (+0.4617) | Flow
2026-05-24 08:28:38 0.0000 | KL 1.8660 | NextKL 1.8705 | SideQ 0% | Score 0.0000 (35.4s)
2026-05-24 08:28:38     Gate FAIL | Improve seed/ref mismatch cur=1.8660 req<=0.0000 prev=mismatch |
2026-05-24 08:28:38 Consist ok ema_cur=1.9526 ema_next=1.9683 ratio=1.008 max<=1.20
2026-05-24 08:28:39   Evicted cached model:
2026-05-24 08:28:39 mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c
2026-05-24 08:28:40   [20/50] UID 79 | Lin2es/evolai-tfm-03o @
2026-05-24 08:28:40 2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600 | hotkey 5D4eNqXRjWmX…
2026-05-24 08:28:40     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:28:40     Fetched 20 texts (20 indices)
2026-05-24 08:28:40    Downloading
2026-05-24 08:28:40 mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba…
2026-05-24 08:28:41     Loaded (local prefetch)
2026-05-24 08:28:41     Model 0.46B → batch=512, seq=16384
2026-05-24 08:28:45    Ready: mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba
2026-05-24 08:29:16     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:32
2026-05-24 08:29:16     Loss 2.2274 | Size ×0.50 | Think 2.2274 | ThinkGain 0 (+0.4565) | Flow
2026-05-24 08:29:16 0.1568 | KL 2.3798 | NextKL 2.6815 | SideQ 0% | Score 0.0000 (34.8s)
2026-05-24 08:29:16     Gate FAIL | Improve seed/ref mismatch cur=2.3798 req<=0.0000 prev=mismatch |
2026-05-24 08:29:16 Consist ok ema_cur=2.4029 ema_next=2.4343 ratio=1.013 max<=1.20
2026-05-24 08:29:17   Evicted cached model:
2026-05-24 08:29:17 mrthor102/evolai-tfm-super-001@f7d9445d9182dd4333dbe32ebd6a7853649a8f41
2026-05-24 08:29:18   [21/50] UID 82 | clear-blue-sky/evolai-reborn-tfm-003 @
2026-05-24 08:29:18 db37ac46734d13b9f00d6049d02ad79254bcd03f | hotkey 5EtDxpyqHywK…
2026-05-24 08:29:18     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:29:18     Fetched 20 texts (20 indices)
2026-05-24 08:29:18    Downloading
2026-05-24 08:29:18 dreamiii0406/evolai-0p47b-v1@fea2659bdf8bd35e5382c50e4857f1ab20f20262…
2026-05-24 08:29:19     Loaded (local prefetch)
2026-05-24 08:29:20     Model 0.46B → batch=512, seq=16384
2026-05-24 08:29:21    Ready: dreamiii0406/evolai-0p47b-v1@fea2659bdf8bd35e5382c50e4857f1ab20f20262
2026-05-24 08:29:56     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:33
2026-05-24 08:29:56     Loss 3.7075 | Size ×0.50 | Think 3.7075 | ThinkGain 0 (+0.4598) | Flow
2026-05-24 08:29:56 0.1898 | KL 1.6882 | NextKL 1.8410 | SideQ 0% | Score 0.0000 (36.2s)
2026-05-24 08:29:56     Gate FAIL | Improve seed/ref mismatch cur=1.6882 req<=0.0000 prev=mismatch |
2026-05-24 08:29:56 Consist ok ema_cur=1.8934 ema_next=1.9174 ratio=1.013 max<=1.20
2026-05-24 08:29:57   Evicted cached model:
2026-05-24 08:29:57 clear-blue-sky/evolai-reborn-tfm-002@3c1af863d3a626ef7f225f335e95f12a17870386
2026-05-24 08:29:58   [22/50] UID 76 | mihai-777/evolai-tfm-1p5b-05 @
2026-05-24 08:29:58 a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba | hotkey 5GLBxPtoiB7R…
2026-05-24 08:29:58     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:29:58     Fetched 20 texts (20 indices)
2026-05-24 08:29:58    Downloading Radiant28/evolai-1p5b@e351598db6d77f85b5081768df04d37c132750f0…
2026-05-24 08:29:59     Loaded (local prefetch)
2026-05-24 08:29:59     Model 0.46B → batch=512, seq=16384
2026-05-24 08:30:04    Ready: Radiant28/evolai-1p5b@e351598db6d77f85b5081768df04d37c132750f0
2026-05-24 08:30:36     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 08:30:36     Loss 2.8645 | Size ×0.50 | Think 2.8645 | ThinkGain 0 (+0.4554) | Flow
2026-05-24 08:30:36 0.0000 | KL 2.7470 | NextKL 1.9994 | SideQ 0% | Score 0.0000 (36.9s)
2026-05-24 08:30:36     Gate FAIL | Improve seed/ref mismatch cur=2.7470 req<=0.0000 prev=mismatch |
2026-05-24 08:30:36 Consist ok ema_cur=2.4986 ema_next=2.4293 ratio=0.972 max<=1.20
2026-05-24 08:30:38   Evicted cached model:
2026-05-24 08:30:38 clear-blue-sky/evolai-reborn-tfm-010@29651f934f3b275247eaca45fd35518d83e94a0d
2026-05-24 08:30:38   [23/50] UID 80 | dreamiii0406/evolai-0p47b-v1 @
2026-05-24 08:30:38 fea2659bdf8bd35e5382c50e4857f1ab20f20262 | hotkey 5Cd2zZyMQnvp…
2026-05-24 08:30:38     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:30:38     Fetched 20 texts (20 indices)
2026-05-24 08:30:38    Downloading
2026-05-24 08:30:38 mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a…
2026-05-24 08:30:40     Loaded (local prefetch)
2026-05-24 08:30:40     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:30:42   [24/50] UID 43 | Radiant28/evolai-1p5b @
2026-05-24 08:30:42 e351598db6d77f85b5081768df04d37c132750f0 | hotkey 5HSz4knZnWHY…
2026-05-24 08:30:42     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:30:42     Fetched 20 texts (20 indices)
2026-05-24 08:30:42    Ready: mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a
2026-05-24 08:30:42    Downloading
2026-05-24 08:30:42 mrthor102/evolai-tfm-super-004@8e2e1c6b0c7c398bcb2c6db8887b2af4679c1f16…
2026-05-24 08:30:44     Loaded (local prefetch)
2026-05-24 08:30:44     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:30:46   [25/50] UID 38 | mihai-777/evolai-tfm-1p5b-alt @
2026-05-24 08:30:46 5ebb4a406916abe39e32823ff1f635b70e707e5a | hotkey 5FbfiXysyCtC…
2026-05-24 08:30:46     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:30:46     Fetched 20 texts (20 indices)
2026-05-24 08:30:47    Ready:
2026-05-24 08:30:47 mrthor102/evolai-tfm-super-004@8e2e1c6b0c7c398bcb2c6db8887b2af4679c1f16
2026-05-24 08:30:47    Downloading
2026-05-24 08:30:47 Radiant28/evolai-0.4b-V1@5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5…
2026-05-24 08:30:47 Fetching 7 files: 100%|██████████| 7/7 [00:06<00:00,  1.11it/s]
2026-05-24 08:30:47     Loaded (local prefetch)
2026-05-24 08:30:48     Model 0.46B → batch=512, seq=16384
2026-05-24 08:30:53    Ready: Radiant28/evolai-0.4b-V1@5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5
2026-05-24 08:31:22     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:31
2026-05-24 08:31:22     Loss 2.8907 | Size ×0.50 | Think 2.8907 | ThinkGain 0 (+0.4537) | Flow
2026-05-24 08:31:22 0.2451 | KL 2.2559 | NextKL 2.4190 | SideQ 0% | Score 0.0000 (33.9s)
2026-05-24 08:31:22     Gate FAIL | Improve seed/ref mismatch cur=2.2559 req<=0.0000 prev=mismatch |
2026-05-24 08:31:22 Consist ok ema_cur=2.3669 ema_next=2.3919 ratio=1.011 max<=1.20
2026-05-24 08:31:23   Evicted cached model:
2026-05-24 08:31:23 mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678
2026-05-24 08:31:23   [26/50] UID 99 | mrthor102/evolai-tfm-super-004 @
2026-05-24 08:31:23 8e2e1c6b0c7c398bcb2c6db8887b2af4679c1f16 | hotkey 5EnuPuwNaqmP…
2026-05-24 08:31:23     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:31:23     Fetched 20 texts (20 indices)
2026-05-24 08:31:23    Downloading evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4…
2026-05-24 08:31:25     Loaded (local prefetch)
2026-05-24 08:31:25     Model 0.46B → batch=512, seq=16384
2026-05-24 08:31:26    Ready: evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4
2026-05-24 08:32:02     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 08:32:03     Loss 4.2079 | Size ×0.50 | Think 4.2079 | ThinkGain 0 (+0.4594) | Flow
2026-05-24 08:32:03 0.0000 | KL 2.0532 | NextKL 1.9794 | SideQ 0% | Score 0.0000 (37.2s)
2026-05-24 08:32:03     Gate FAIL | Improve seed/ref mismatch cur=2.0532 req<=0.0000 prev=mismatch |
2026-05-24 08:32:03 Consist ok ema_cur=1.9582 ema_next=1.9538 ratio=0.998 max<=1.20
2026-05-24 08:32:04   Evicted cached model:
2026-05-24 08:32:04 mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a
2026-05-24 08:32:05   [27/50] UID 44 | Radiant28/evolai-0.4b-V1 @
2026-05-24 08:32:05 5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5 | hotkey 5DXm2ShZGmwG…
2026-05-24 08:32:05     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:32:05     Fetched 20 texts (20 indices)
2026-05-24 08:32:05    Downloading philk11/evolai-0.4b@822950352d63cdd145c3a7449ebfd4b51ad5ae6a…
2026-05-24 08:32:07     Loaded (local prefetch)
2026-05-24 08:32:07     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:32:08    Ready: philk11/evolai-0.4b@822950352d63cdd145c3a7449ebfd4b51ad5ae6a
2026-05-24 08:32:09   [28/50] UID 95 | evolai/evolai_naive_kl @
2026-05-24 08:32:09 da8203b6900f14ec1b724f3dd8c6dc35576fc3e4 | hotkey 5CXwmm7R4U6o…
2026-05-24 08:32:09     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:32:09    Downloading
2026-05-24 08:32:09 Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9…
2026-05-24 08:32:09     Fetched 20 texts (20 indices)
2026-05-24 08:32:10     Loaded (local prefetch)
2026-05-24 08:32:10     Model 0.46B → batch=512, seq=16384
2026-05-24 08:32:13    Ready: Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9
2026-05-24 08:32:45     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:32
2026-05-24 08:32:45     Loss 2.5799 | Size ×0.50 | Think 2.5799 | ThinkGain 0 (+0.4848) | Flow
2026-05-24 08:32:45 0.0166 | KL 2.8590 | NextKL 2.6833 | SideQ 0% | Score 0.0000 (34.5s)
2026-05-24 08:32:45     Gate FAIL | Improve seed/ref mismatch cur=2.8590 req<=0.0000 prev=mismatch |
2026-05-24 08:32:45 Consist ok ema_cur=2.8644 ema_next=2.8292 ratio=0.988 max<=1.20
2026-05-24 08:32:47   Evicted cached model:
2026-05-24 08:32:47 clear-blue-sky/evolai-reborn-tfm-006@27bbbdbe12605a00573f2af96d1d99d61e430ce6
2026-05-24 08:32:47   [29/50] UID 65 | philk11/evolai-0.4b @
2026-05-24 08:32:47 822950352d63cdd145c3a7449ebfd4b51ad5ae6a | hotkey 5GvHE1tHbhGv…
2026-05-24 08:32:47     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:32:47     Fetched 20 texts (20 indices)
2026-05-24 08:32:47    Downloading
2026-05-24 08:32:47 andrebarrosilva1123/evolai-f@89654c7b1e351cce36bab65fe09692eb0e109f72…
2026-05-24 08:32:48     Loaded (local prefetch)
2026-05-24 08:32:49     ⚠ Invalid model size (0.60B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 08:32:50   [30/50] UID 93 | Phoenix9781/evolai-tf-model @
2026-05-24 08:32:50 b05038fcfdcc79fa8d8e79730074b65cd68c73f9 | hotkey 5F4R25t78FSF…
2026-05-24 08:32:50     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:32:50     Fetched 20 texts (20 indices)
2026-05-24 08:32:52     Loaded (local prefetch)
2026-05-24 08:32:52     Model 0.46B → batch=512, seq=16384
2026-05-24 08:32:53    Ready: andrebarrosilva1123/evolai-f@89654c7b1e351cce36bab65fe09692eb0e109f72
2026-05-24 08:32:53    Downloading
2026-05-24 08:32:53 clear-blue-sky/evolai-reborn-tfm-004@6e3b9a12cfe424e71568aedf62377377d49e4346…
2026-05-24 08:32:53 Fetching 7 files: 100%|██████████| 7/7 [00:03<00:00,  1.96it/s]
2026-05-24 08:32:57    Ready:
2026-05-24 08:32:57 clear-blue-sky/evolai-reborn-tfm-004@6e3b9a12cfe424e71568aedf62377377d49e4346
2026-05-24 08:33:30     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 08:33:30     Loss 3.8102 | Size ×0.50 | Think 3.8102 | ThinkGain 0 (+0.4581) | Flow
2026-05-24 08:33:30 0.0169 | KL 1.9333 | NextKL 2.1836 | SideQ 0% | Score 0.0000 (37.5s)
2026-05-24 08:33:30     Gate FAIL | Improve seed/ref mismatch cur=1.9333 req<=0.0000 prev=mismatch |
2026-05-24 08:33:30 Consist ok ema_cur=1.9503 ema_next=1.9643 ratio=1.007 max<=1.20
2026-05-24 08:33:32   Evicted cached model:
2026-05-24 08:33:32 clear-blue-sky/evolai-reborn-tfm-007@ba9045012f93d80b69da2201376756708f45f355
2026-05-24 08:33:32   [31/50] UID 52 | andrebarrosilva1123/evolai-f @
2026-05-24 08:33:32 89654c7b1e351cce36bab65fe09692eb0e109f72 | hotkey 5HTZZEb5oxv9…
2026-05-24 08:33:32    Downloading
2026-05-24 08:33:32 evolai/evolai_test_challenge@c9122c31993eb1d9385cd65d609605619ec92d9b…
2026-05-24 08:33:32     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:33:32     Fetched 20 texts (20 indices)
2026-05-24 08:33:34     Loaded (local prefetch)
2026-05-24 08:33:35     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:33:36    Ready: evolai/evolai_test_challenge@c9122c31993eb1d9385cd65d609605619ec92d9b
2026-05-24 08:33:37   [32/50] UID 70 | clear-blue-sky/evolai-reborn-tfm-004 @
2026-05-24 08:33:37 6e3b9a12cfe424e71568aedf62377377d49e4346 | hotkey 5Hdg2gHopWQK…
2026-05-24 08:33:37     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:33:37     Fetched 20 texts (20 indices)
2026-05-24 08:33:37    Downloading
2026-05-24 08:33:37 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb…
2026-05-24 08:33:38     Loaded (local prefetch)
2026-05-24 08:33:39     Model 0.46B → batch=512, seq=16384
2026-05-24 08:33:41    Ready:
2026-05-24 08:33:41 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb
2026-05-24 08:34:16     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 08:34:16     Loss 4.0898 | Size ×0.50 | Think 4.0898 | ThinkGain 0 (+0.4639) | Flow
2026-05-24 08:34:16 0.0000 | KL 1.9655 | NextKL 1.9158 | SideQ 0% | Score 0.0000 (37.2s)
2026-05-24 08:34:16     Gate FAIL | Improve seed/ref mismatch cur=1.9655 req<=0.0000 prev=mismatch |
2026-05-24 08:34:16 Consist ok ema_cur=1.9030 ema_next=1.9056 ratio=1.001 max<=1.20
2026-05-24 08:34:17   Evicted cached model:
2026-05-24 08:34:17 Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600
2026-05-24 08:34:18   [33/50] UID 8 | evolai/evolai_test_challenge @
2026-05-24 08:34:18 c9122c31993eb1d9385cd65d609605619ec92d9b | hotkey 5ENhqnBoyFdz…
2026-05-24 08:34:18     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:34:18     Fetched 20 texts (20 indices)
2026-05-24 08:34:18    Downloading
2026-05-24 08:34:18 Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002…
2026-05-24 08:34:19     Loaded (local prefetch)
2026-05-24 08:34:20     Model 0.46B → batch=512, seq=16384
2026-05-24 08:34:22    Ready: Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002
2026-05-24 08:34:57     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 08:34:57     Loss 3.6027 | Size ×0.50 | Think 3.6027 | ThinkGain 0 (+0.4518) | Flow
2026-05-24 08:34:57 0.0171 | KL 1.7487 | NextKL 1.9632 | SideQ 0% | Score 0.0000 (37.4s)
2026-05-24 08:34:57     Gate FAIL | Improve seed/ref mismatch cur=1.7487 req<=0.0000 prev=mismatch |
2026-05-24 08:34:57 Consist ok ema_cur=1.7302 ema_next=1.9454 ratio=1.124 max<=1.20
2026-05-24 08:34:59   Evicted cached model:
2026-05-24 08:34:59 clear-blue-sky/evolai-reborn-tfm-003@db37ac46734d13b9f00d6049d02ad79254bcd03f
2026-05-24 08:34:59   [34/50] UID 48 | sangerno63/evolai-transformer-v2 @
2026-05-24 08:34:59 4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb | hotkey 5ED3KNj5uEVS…
2026-05-24 08:34:59     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:34:59     Fetched 20 texts (20 indices)
2026-05-24 08:34:59    Downloading Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d…
2026-05-24 08:35:01     Loaded (local prefetch)
2026-05-24 08:35:01     Model 0.46B → batch=512, seq=16384
2026-05-24 08:35:03    Ready: Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d
2026-05-24 08:35:35     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:31
2026-05-24 08:35:36     Loss 4.1999 | Size ×0.50 | Think 4.1999 | ThinkGain 0 (+0.4473) | Flow
2026-05-24 08:35:36 0.0000 | KL 2.3440 | NextKL 1.9501 | SideQ 0% | Score 0.0000 (34.1s)
2026-05-24 08:35:36     Gate FAIL | Improve seed/ref mismatch cur=2.3440 req<=0.0000 prev=mismatch |
2026-05-24 08:35:36 Consist ok ema_cur=2.2160 ema_next=2.1799 ratio=0.984 max<=1.20
2026-05-24 08:35:37   Evicted cached model:
2026-05-24 08:35:37 mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba
2026-05-24 08:35:38   [35/50] UID 100 | Danieli1021/evolai-qwen047-v3 @
2026-05-24 08:35:38 e01dfd3b9c54325c98bf12966bdebadace391002 | hotkey 5DMH2VrrukYd…
2026-05-24 08:35:38     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:35:38     Fetched 20 texts (20 indices)
2026-05-24 08:35:38    Downloading galuis116/evolai-future@9e86122b813ff73727cbe5711727895bd03d293a…
2026-05-24 08:35:39     Loaded (local prefetch)
2026-05-24 08:35:39     Model 0.47B → batch=512, seq=16384
2026-05-24 08:35:42    Ready: galuis116/evolai-future@9e86122b813ff73727cbe5711727895bd03d293a
2026-05-24 08:35:58     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:16
2026-05-24 08:35:59     Loss 4.1601 | Size ×0.51 | Think 4.1601 | ThinkGain 0 (+0.4819) | Flow
2026-05-24 08:35:59 0.0000 | KL 4.1897 | NextKL 3.8966 | SideQ 0% | Score 0.0000 (19.1s)
2026-05-24 08:35:59     Gate FAIL | Improve seed/ref mismatch cur=4.1897 req<=0.0000 prev=mismatch |
2026-05-24 08:35:59 Consist ok ema_cur=4.5086 ema_next=3.9373 ratio=0.873 max<=1.20
2026-05-24 08:35:59   Evicted cached model:
2026-05-24 08:35:59 mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a
2026-05-24 08:36:00   [36/50] UID 77 | Lin2es/evolai-tfm-01o @
2026-05-24 08:36:00 d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d | hotkey 5GQydjNVEhMb…
2026-05-24 08:36:00     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:36:00     Fetched 20 texts (20 indices)
2026-05-24 08:36:00    Downloading
2026-05-24 08:36:00 clear-blue-sky/evolai-reborn-tfm-009@8b9297c32ac0472e1ac5165bbad3f96aac68a159…
2026-05-24 08:36:02     Loaded (local prefetch)
2026-05-24 08:36:02     Model 0.46B → batch=512, seq=16384
2026-05-24 08:36:05    Ready:
2026-05-24 08:36:05 clear-blue-sky/evolai-reborn-tfm-009@8b9297c32ac0472e1ac5165bbad3f96aac68a159
2026-05-24 08:36:38     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:33
2026-05-24 08:36:39     Loss 2.8218 | Size ×0.50 | Think 2.8218 | ThinkGain 0 (+0.4381) | Flow
2026-05-24 08:36:39 0.0000 | KL 2.7014 | NextKL 2.3550 | SideQ 0% | Score 0.0000 (36.4s)
2026-05-24 08:36:39     Gate FAIL | Improve seed/ref mismatch cur=2.7014 req<=0.0000 prev=mismatch |
2026-05-24 08:36:39 Consist ok ema_cur=2.6526 ema_next=2.6006 ratio=0.980 max<=1.20
2026-05-24 08:36:40   Evicted cached model:
2026-05-24 08:36:40 mrthor102/evolai-tfm-super-004@8e2e1c6b0c7c398bcb2c6db8887b2af4679c1f16
2026-05-24 08:36:41   [37/50] UID 101 | galuis116/evolai-future @
2026-05-24 08:36:41 9e86122b813ff73727cbe5711727895bd03d293a | hotkey 5DPz76uobJLT…
2026-05-24 08:36:41     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:36:41     Fetched 20 texts (20 indices)
2026-05-24 08:36:41    Downloading
2026-05-24 08:36:41 andrebarrosilva1123/evolai-d@89649e9376dace64f631711d3d270198e376702e…
2026-05-24 08:36:42     Loaded (local prefetch)
2026-05-24 08:36:42     Model 0.46B → batch=512, seq=16384
2026-05-24 08:36:47    Ready: andrebarrosilva1123/evolai-d@89649e9376dace64f631711d3d270198e376702e
2026-05-24 08:37:19     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 08:37:19     Loss 3.8400 | Size ×0.50 | Think 3.8400 | ThinkGain 0 (+0.4596) | Flow
2026-05-24 08:37:19 0.2269 | KL 1.8151 | NextKL 1.7305 | SideQ 0% | Score 0.0000 (36.5s)
2026-05-24 08:37:19     Gate FAIL | Improve seed/ref mismatch cur=1.8151 req<=0.0000 prev=mismatch |
2026-05-24 08:37:19 Consist ok ema_cur=1.9082 ema_next=1.8917 ratio=0.991 max<=1.20
2026-05-24 08:37:21   Evicted cached model:
2026-05-24 08:37:21 evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4
2026-05-24 08:37:21   [38/50] UID 69 | clear-blue-sky/evolai-reborn-tfm-009 @
2026-05-24 08:37:21 8b9297c32ac0472e1ac5165bbad3f96aac68a159 | hotkey 5ChUCf3NjrgS…
2026-05-24 08:37:21     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:37:21     Fetched 20 texts (20 indices)
2026-05-24 08:37:21    Downloading
2026-05-24 08:37:21 andrebarrosilva1123/evolai-c@6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c…
2026-05-24 08:37:22     Loaded (local prefetch)
2026-05-24 08:37:23     Model 0.46B → batch=512, seq=16384
2026-05-24 08:37:28    Ready: andrebarrosilva1123/evolai-c@6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c
2026-05-24 08:38:00     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 08:38:00     Loss 3.9368 | Size ×0.50 | Think 3.9368 | ThinkGain 0 (+0.4622) | Flow
2026-05-24 08:38:00 0.2604 | KL 2.0164 | NextKL 1.6814 | SideQ 0% | Score 0.0000 (37.1s)
2026-05-24 08:38:00     Gate FAIL | Improve seed/ref mismatch cur=2.0164 req<=0.0000 prev=mismatch |
2026-05-24 08:38:00 Consist ok ema_cur=1.9247 ema_next=1.9065 ratio=0.991 max<=1.20
2026-05-24 08:38:02   Evicted cached model:
2026-05-24 08:38:02 Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9
2026-05-24 08:38:02   [39/50] UID 51 | andrebarrosilva1123/evolai-d @
2026-05-24 08:38:02 89649e9376dace64f631711d3d270198e376702e | hotkey 5EhLiPB1GHwH…
2026-05-24 08:38:02     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:38:02     Fetched 20 texts (20 indices)
2026-05-24 08:38:02    Downloading
2026-05-24 08:38:02 Roystar/evolai-qwen2.5-1.5b@47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1…
2026-05-24 08:38:04     Loaded (local prefetch)
2026-05-24 08:38:05     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:38:07   [40/50] UID 54 | andrebarrosilva1123/evolai-c @
2026-05-24 08:38:07 6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c | hotkey 5D7HPRR2QdDB…
2026-05-24 08:38:07     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:38:07     Fetched 20 texts (20 indices)
2026-05-24 08:38:09    Ready: Roystar/evolai-qwen2.5-1.5b@47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1
2026-05-24 08:38:09    Downloading Jubilant/evolai-1.54b@d8681d30b14cb5a597d2ff7c909998cf9d217599…
2026-05-24 08:38:09     Loaded (local prefetch)
2026-05-24 08:38:09 Fetching 7 files: 100%|██████████| 7/7 [00:06<00:00,  1.08it/s]
2026-05-24 08:38:09     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:38:11   [41/50] UID 55 | Roystar/evolai-qwen2.5-1.5b @
2026-05-24 08:38:11 47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1 | hotkey 5DhRJtUeVA6P…
2026-05-24 08:38:11     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:38:11     Fetched 20 texts (20 indices)
2026-05-24 08:38:13     Loaded (local prefetch)
2026-05-24 08:38:14     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:38:15    Ready: Jubilant/evolai-1.54b@d8681d30b14cb5a597d2ff7c909998cf9d217599
2026-05-24 08:38:15    Downloading Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59…
2026-05-24 08:38:16   [42/50] UID 36 | Jubilant/evolai-1.54b @
2026-05-24 08:38:16 d8681d30b14cb5a597d2ff7c909998cf9d217599 | hotkey 5G7Co5VNfQio…
2026-05-24 08:38:16     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:38:16     Fetched 20 texts (20 indices)
2026-05-24 08:38:18     Loaded (local prefetch)
2026-05-24 08:38:18     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:38:19    Ready: Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59
2026-05-24 08:38:19    Downloading
2026-05-24 08:38:19 clear-blue-sky/evolai-reborn-tfm-001@a9b8015b9bcc040b74f8c328190566bef5b1d25e…
2026-05-24 08:38:20   [43/50] UID 78 | Lin2es/evolai-tfm-02o @
2026-05-24 08:38:20 fc5fc3ee4a3877b825b404dc85c9367c1f248c59 | hotkey 5FA2kgLNs36d…
2026-05-24 08:38:20     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:38:20     Fetched 20 texts (20 indices)
2026-05-24 08:38:21     Loaded (local prefetch)
2026-05-24 08:38:22     Model 0.46B → batch=512, seq=16384
2026-05-24 08:38:24    Ready:
2026-05-24 08:38:24 clear-blue-sky/evolai-reborn-tfm-001@a9b8015b9bcc040b74f8c328190566bef5b1d25e
2026-05-24 08:38:24    Downloading
2026-05-24 08:38:24 Jubilant/evolai-1.50b-v1@074810c41bab77c52a216e0c2f7886484e12deeb…
2026-05-24 08:38:24 Fetching 7 files: 100%|██████████| 7/7 [00:06<00:00,  1.09it/s]
2026-05-24 08:38:31    Ready: Jubilant/evolai-1.50b-v1@074810c41bab77c52a216e0c2f7886484e12deeb
2026-05-24 08:38:59     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 08:38:59     Loss 2.9082 | Size ×0.50 | Think 2.9082 | ThinkGain 0 (+0.4256) | Flow
2026-05-24 08:38:59 0.0000 | KL 2.8450 | NextKL 2.8060 | SideQ 0% | Score 0.0000 (37.5s)
2026-05-24 08:38:59     Gate FAIL | Improve seed/ref mismatch cur=2.8450 req<=0.0000 prev=mismatch |
2026-05-24 08:38:59 Consist ok ema_cur=2.8081 ema_next=2.8042 ratio=0.999 max<=1.20
2026-05-24 08:39:00   Evicted cached model:
2026-05-24 08:39:00 clear-blue-sky/evolai-reborn-tfm-004@6e3b9a12cfe424e71568aedf62377377d49e4346
2026-05-24 08:39:01   [44/50] UID 62 | clear-blue-sky/evolai-reborn-tfm-001 @
2026-05-24 08:39:01 a9b8015b9bcc040b74f8c328190566bef5b1d25e | hotkey 5EjjVuNJsjqP…
2026-05-24 08:39:01    Downloading
2026-05-24 08:39:01 dexserbia/evolai-gemma2-9b@7fe66309a3847239a4da5b712477f2105e88399b…
2026-05-24 08:39:01     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:39:01     Fetched 20 texts (20 indices)
2026-05-24 08:39:03     Loaded (local prefetch)
2026-05-24 08:39:03     Model 0.46B → batch=512, seq=16384
2026-05-24 08:39:32    Ready: dexserbia/evolai-gemma2-9b@7fe66309a3847239a4da5b712477f2105e88399b
2026-05-24 08:39:43     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:37
2026-05-24 08:39:43     Loss 4.0717 | Size ×0.50 | Think 4.0717 | ThinkGain 0 (+0.4623) | Flow
2026-05-24 08:39:43 0.0000 | KL 2.0717 | NextKL 1.8757 | SideQ 0% | Score 0.0000 (39.5s)
2026-05-24 08:39:43     Gate FAIL | Improve seed/ref mismatch cur=2.0717 req<=0.0000 prev=mismatch |
2026-05-24 08:39:43 Consist ok ema_cur=1.9533 ema_next=1.9239 ratio=0.985 max<=1.20
2026-05-24 08:39:44   Evicted cached model:
2026-05-24 08:39:44 evolai/evolai_test_challenge@c9122c31993eb1d9385cd65d609605619ec92d9b
2026-05-24 08:39:45   [45/50] UID 40 | Jubilant/evolai-1.50b-v1 @
2026-05-24 08:39:45 074810c41bab77c52a216e0c2f7886484e12deeb | hotkey 5Fuv43yR7tjJ…
2026-05-24 08:39:45     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:39:45     Fetched 20 texts (20 indices)
2026-05-24 08:39:45    Downloading
2026-05-24 08:39:45 clear-blue-sky/evolai-reborn-tfm-005@4e2c98f78611b6f2e63d6baad12b51c589f8afb3…
2026-05-24 08:39:46     Loaded (local prefetch)
2026-05-24 08:39:47     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:39:49   [46/50] UID 9 | dexserbia/evolai-gemma2-9b @
2026-05-24 08:39:49 7fe66309a3847239a4da5b712477f2105e88399b | hotkey 5EbpxBkVKVNV…
2026-05-24 08:39:49     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:39:49     Fetched 20 texts (20 indices)
2026-05-24 08:39:49    Ready:
2026-05-24 08:39:49 clear-blue-sky/evolai-reborn-tfm-005@4e2c98f78611b6f2e63d6baad12b51c589f8afb3
2026-05-24 08:39:49    Downloading Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4…
2026-05-24 08:39:51    Ready: Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4
2026-05-24 08:39:54     Loaded (local prefetch)
2026-05-24 08:39:56     ⚠ Invalid model size (9.24B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 08:39:58   [47/50] UID 83 | clear-blue-sky/evolai-reborn-tfm-005 @
2026-05-24 08:39:58 4e2c98f78611b6f2e63d6baad12b51c589f8afb3 | hotkey 5G8tRiKdn5cC…
2026-05-24 08:39:58     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:39:58     Fetched 20 texts (20 indices)
2026-05-24 08:39:58    Downloading
2026-05-24 08:39:58 batster4/evolai-phi4-mini-dpo-v1@8217794abaf74f8e15f578a507e27b5f9b1df4c9…
2026-05-24 08:40:00     Loaded (local prefetch)
2026-05-24 08:40:00     Model 0.46B → batch=512, seq=16384
2026-05-24 08:40:13    Ready:
2026-05-24 08:40:13 batster4/evolai-phi4-mini-dpo-v1@8217794abaf74f8e15f578a507e27b5f9b1df4c9
2026-05-24 08:40:38     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 08:40:39     Loss 3.7473 | Size ×0.50 | Think 3.7473 | ThinkGain 0 (+0.4632) | Flow
2026-05-24 08:40:39 0.0000 | KL 1.9585 | NextKL 1.8621 | SideQ 0% | Score 0.0000 (38.3s)
2026-05-24 08:40:39     Gate FAIL | Improve seed/ref mismatch cur=1.9585 req<=0.0000 prev=mismatch |
2026-05-24 08:40:39 Consist ok ema_cur=2.6802 ema_next=1.9396 ratio=0.724 max<=1.20
2026-05-24 08:40:40   Evicted cached model:
2026-05-24 08:40:40 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb
2026-05-24 08:40:40   [48/50] UID 92 | Lin2es/evolai-tfm-04o @
2026-05-24 08:40:40 52061d203723fdc8be09324d0c827898fcb7bdc4 | hotkey 5GefYX69KUVQ…
2026-05-24 08:40:40     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:40:40    Downloading
2026-05-24 08:40:40 clear-blue-sky/evolai-reborn-tfm-008@47961a2955038f307126b383cedfcaf3c83fc00e…
2026-05-24 08:40:40     Fetched 20 texts (20 indices)
2026-05-24 08:40:42     Loaded (local prefetch)
2026-05-24 08:40:42     Model 0.46B → batch=512, seq=16384
2026-05-24 08:40:45    Ready:
2026-05-24 08:40:45 clear-blue-sky/evolai-reborn-tfm-008@47961a2955038f307126b383cedfcaf3c83fc00e
2026-05-24 08:41:16     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:31
2026-05-24 08:41:17     Loss 2.9164 | Size ×0.50 | Think 2.9164 | ThinkGain 0 (+0.4483) | Flow
2026-05-24 08:41:17 0.0000 | KL 2.4377 | NextKL 2.1930 | SideQ 0% | Score 0.0000 (34.1s)
2026-05-24 08:41:17     Gate FAIL | Improve seed/ref mismatch cur=2.4377 req<=0.0000 prev=mismatch |
2026-05-24 08:41:17 Consist ok ema_cur=3.2060 ema_next=2.5218 ratio=0.787 max<=1.20
2026-05-24 08:41:17   Evicted cached model:
2026-05-24 08:41:17 Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002
2026-05-24 08:41:18   [49/50] UID 59 | batster4/evolai-phi4-mini-dpo-v1 @
2026-05-24 08:41:18 8217794abaf74f8e15f578a507e27b5f9b1df4c9 | hotkey 5GCA2s6m4RRM…
2026-05-24 08:41:18     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:41:18     Fetched 20 texts (20 indices)
2026-05-24 08:41:21     Loaded (local prefetch)
2026-05-24 08:41:22     ⚠ Invalid model size (3.84B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 08:41:23   [50/50] UID 85 | clear-blue-sky/evolai-reborn-tfm-008 @
2026-05-24 08:41:23 47961a2955038f307126b383cedfcaf3c83fc00e | hotkey 5EC5MzPj6dGb…
2026-05-24 08:41:23     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:41:23     Fetched 20 texts (20 indices)
2026-05-24 08:41:24     Loaded (local prefetch)
2026-05-24 08:41:25     Model 0.46B → batch=512, seq=16384
2026-05-24 08:41:58     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:30
2026-05-24 08:41:58     Loss 3.8056 | Size ×0.50 | Think 3.8056 | ThinkGain 0 (+0.4616) | Flow
2026-05-24 08:41:58 0.0000 | KL 1.9754 | NextKL 2.0239 | SideQ 0% | Score 0.0000 (33.0s)
2026-05-24 08:41:58     Gate FAIL | Improve seed/ref mismatch cur=1.9754 req<=0.0000 prev=mismatch |
2026-05-24 08:41:58 Consist ok ema_cur=2.6665 ema_next=1.9659 ratio=0.737 max<=1.20
2026-05-24 08:41:59   Evicted cached model:
2026-05-24 08:41:59 Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d
2026-05-24 08:42:00   Cached next refs for transformer: 50 miner(s)
2026-05-24 08:42:00 
2026-05-24 08:42:00   ✓ TRANSFORMER: 30 evaluated, 23 skipped —
2026-05-24 08:42:00 epoch_22924_transformer_20260524_081230.json
2026-05-24 08:42:00   ✓ Telemetry sent (30 records)
2026-05-24 08:42:00 Evaluating MAMBA2 track…
2026-05-24 08:42:00 
2026-05-24 08:42:00   Found 15 locked mamba2 miners
2026-05-24 08:42:00    Downloading Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8…
2026-05-24 08:42:00 Pre-building current/next challenges for 15 miners…
2026-05-24 08:42:00 Fetching 7 files: 100%|██████████| 7/7 [00:02<00:00,  2.50it/s]
2026-05-24 08:42:03    Ready: Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8
2026-05-24 08:42:03    Downloading
2026-05-24 08:42:03 elgin-group/evolai-mamba2-0p47b-v1@39b2f90ad08643d34503c88f5c7224fd3dabeed7…
2026-05-24 08:42:03 Fetching 8 files: 100%|██████████| 8/8 [00:03<00:00,  2.24it/s]
2026-05-24 08:42:08    Ready:
2026-05-24 08:42:08 elgin-group/evolai-mamba2-0p47b-v1@39b2f90ad08643d34503c88f5c7224fd3dabeed7
2026-05-24 08:42:37 ✓ Ref data ready: submitted=30, cached=0
2026-05-24 08:42:37   [1/15] UID 90 | Lin2es/evolai-mb2-02v @
2026-05-24 08:42:37 c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8 | hotkey 5CtLLhrw6Lxa…
2026-05-24 08:42:37     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:42:37     Fetched 20 texts (20 indices)
2026-05-24 08:42:37    Downloading
2026-05-24 08:42:37 andrebarrosilva1123/evolai-mamba2-a@55b92d373b1c219a4cfbac7034c154ddbcdc854d…
2026-05-24 08:42:40    Ready:
2026-05-24 08:42:40 andrebarrosilva1123/evolai-mamba2-a@55b92d373b1c219a4cfbac7034c154ddbcdc854d
2026-05-24 08:42:47     Loaded (local prefetch)
2026-05-24 08:42:47     Model 0.48B → batch=512, seq=16384
2026-05-24 08:43:09     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:16
2026-05-24 08:43:09     Loss 4.6753 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 08:43:09 0.0000 | KL 4.6753 | NextKL 4.7356 | SideQ 0% | Score 0.0000 (22.0s)
2026-05-24 08:43:09     Gate FAIL | Improve seed/ref mismatch cur=4.6753 req<=0.0000 prev=mismatch |
2026-05-24 08:43:09 Consist ok ema_cur=5.1888 ema_next=4.7152 ratio=0.909 max<=1.20
2026-05-24 08:43:11   Evicted cached model:
2026-05-24 08:43:11 galuis116/evolai-future@9e86122b813ff73727cbe5711727895bd03d293a
2026-05-24 08:43:12   [2/15] UID 34 | elgin-group/evolai-mamba2-0p47b-v1 @
2026-05-24 08:43:12 39b2f90ad08643d34503c88f5c7224fd3dabeed7 | hotkey 5GNJr9NfE9e9…
2026-05-24 08:43:12     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:43:12     Fetched 20 texts (20 indices)
2026-05-24 08:43:12    Downloading
2026-05-24 08:43:12 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c…
2026-05-24 08:43:15    Ready:
2026-05-24 08:43:15 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c
2026-05-24 08:43:16     Loaded (local prefetch)
2026-05-24 08:43:17     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 08:43:18   [3/15] UID 56 | andrebarrosilva1123/evolai-mamba2-a @
2026-05-24 08:43:18 55b92d373b1c219a4cfbac7034c154ddbcdc854d | hotkey 5D1zGn2n3mzF…
2026-05-24 08:43:18     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:43:18     Fetched 20 texts (20 indices)
2026-05-24 08:43:18    Downloading
2026-05-24 08:43:18 andrebarrosilva1123/evolai-mamba2-b@62336a49df6d6014f779575adfd29373c228edd4…
2026-05-24 08:43:21    Ready:
2026-05-24 08:43:21 andrebarrosilva1123/evolai-mamba2-b@62336a49df6d6014f779575adfd29373c228edd4
2026-05-24 08:43:23     Loaded (local prefetch)
2026-05-24 08:43:23     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 08:43:25   [4/15] UID 32 | mihai-777/evolai-mamba2-1p6b-alt @
2026-05-24 08:43:25 131bd3907f9816bbf184f5651ba63af66046e84c | hotkey 5GL84HKDau7C…
2026-05-24 08:43:25     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:43:25    Downloading
2026-05-24 08:43:25 Radiant28/evolai-mamba2-0.47b-v3@97f692fb0b295aa29075d3f9d592bfb4e7625b16…
2026-05-24 08:43:25     Fetched 20 texts (20 indices)
2026-05-24 08:43:28    Ready:
2026-05-24 08:43:28 Radiant28/evolai-mamba2-0.47b-v3@97f692fb0b295aa29075d3f9d592bfb4e7625b16
2026-05-24 08:43:29     Loaded (local prefetch)
2026-05-24 08:43:30     Model 0.48B → batch=512, seq=16384
2026-05-24 08:43:31    alpha=0.005459 TAO/α  budget=0.049646
2026-05-24 08:43:38     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:04
2026-05-24 08:43:38     Loss 5.0221 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 08:43:38 0.0000 | KL 5.0221 | NextKL 4.7938 | SideQ 0% | Score 0.0000 (7.9s)
2026-05-24 08:43:38     Gate FAIL | Improve seed/ref mismatch cur=5.0221 req<=0.0000 prev=mismatch |
2026-05-24 08:43:38 Consist ok ema_cur=4.8986 ema_next=4.8772 ratio=0.996 max<=1.20
2026-05-24 08:43:40   Evicted cached model:
2026-05-24 08:43:40 clear-blue-sky/evolai-reborn-tfm-009@8b9297c32ac0472e1ac5165bbad3f96aac68a159
2026-05-24 08:43:40   [5/15] UID 57 | andrebarrosilva1123/evolai-mamba2-b @
2026-05-24 08:43:40 62336a49df6d6014f779575adfd29373c228edd4 | hotkey 5EZx1DRvpMGK…
2026-05-24 08:43:40     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:43:40    Downloading Lin2es/evolai-mb2-04v@9c0198682f16cc8595fec849aa37227f7160e92c…
2026-05-24 08:43:40     Fetched 20 texts (20 indices)
2026-05-24 08:43:42     Loaded (local prefetch)
2026-05-24 08:43:43     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 08:43:43    Ready: Lin2es/evolai-mb2-04v@9c0198682f16cc8595fec849aa37227f7160e92c
2026-05-24 08:43:44   [6/15] UID 41 | Radiant28/evolai-mamba2-0.47b-v3 @
2026-05-24 08:43:44 97f692fb0b295aa29075d3f9d592bfb4e7625b16 | hotkey 5CP5QrWuFe93…
2026-05-24 08:43:44     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:43:44     Fetched 20 texts (20 indices)
2026-05-24 08:43:44    Downloading
2026-05-24 08:43:44 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518…
2026-05-24 08:43:47     Loaded (local prefetch)
2026-05-24 08:43:47     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 08:43:48    Ready:
2026-05-24 08:43:48 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518
2026-05-24 08:43:49   [7/15] UID 89 | Lin2es/evolai-mb2-04v @
2026-05-24 08:43:49 9c0198682f16cc8595fec849aa37227f7160e92c | hotkey 5DkZf6V3X8Za…
2026-05-24 08:43:49     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:43:49     Fetched 20 texts (20 indices)
2026-05-24 08:43:49    Downloading Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd…
2026-05-24 08:43:50     Loaded (local prefetch)
2026-05-24 08:43:51     ⚠ Vocab incompatible (model=151665 < ref=248077) — skipping
2026-05-24 08:43:51    Ready: Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd
2026-05-24 08:43:53   [8/15] UID 30 | mihai-777/evolai-mamba2-0p47b-v3 @
2026-05-24 08:43:53 c2a96b92acf632d51a2c21da4482f77f98256518 | hotkey 5GGsbuVKDrTA…
2026-05-24 08:43:53     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:43:53     Fetched 20 texts (20 indices)
2026-05-24 08:43:53    Downloading
2026-05-24 08:43:53 mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7…
2026-05-24 08:43:54     Loaded (local prefetch)
2026-05-24 08:43:54     Model 0.48B → batch=512, seq=16384
2026-05-24 08:43:56    Ready: mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7
2026-05-24 08:43:59     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 08:43:59     Loss 4.7515 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 08:43:59 0.2275 | KL 4.7515 | NextKL 4.8587 | SideQ 0% | Score 0.0000 (4.2s)
2026-05-24 08:43:59     Gate FAIL | Improve seed/ref mismatch cur=4.7515 req<=0.0000 prev=mismatch |
2026-05-24 08:43:59 Consist ok ema_cur=4.7885 ema_next=4.8020 ratio=1.003 max<=1.20
2026-05-24 08:44:00   Evicted cached model:
2026-05-24 08:44:00 Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59
2026-05-24 08:44:01   [9/15] UID 91 | Lin2es/evolai-mb2-03v @
2026-05-24 08:44:01 3047597c4e4b4430450ddcd633240b88d781fdbd | hotkey 5EcdUqvUBCSp…
2026-05-24 08:44:01     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:44:01     Fetched 20 texts (20 indices)
2026-05-24 08:44:01    Downloading Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0…
2026-05-24 08:44:02     Loaded (local prefetch)
2026-05-24 08:44:03     Model 0.48B → batch=512, seq=16384
2026-05-24 08:44:04    Ready: Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0
2026-05-24 08:44:07     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 08:44:07     Loss 4.6669 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 08:44:07 0.0066 | KL 4.6669 | NextKL 4.7157 | SideQ 0% | Score 0.0000 (4.2s)
2026-05-24 08:44:07     Gate FAIL | Improve seed/ref mismatch cur=4.6669 req<=0.0000 prev=mismatch |
2026-05-24 08:44:07 Consist ok ema_cur=4.6624 ema_next=4.6713 ratio=1.002 max<=1.20
2026-05-24 08:44:09   Evicted cached model:
2026-05-24 08:44:09 clear-blue-sky/evolai-reborn-tfm-001@a9b8015b9bcc040b74f8c328190566bef5b1d25e
2026-05-24 08:44:09   [10/15] UID 31 | mihai-777/evolai-mamba2-0p47b @
2026-05-24 08:44:09 7b6564c9a46f602702c260185aa43867f321dee7 | hotkey 5CJuKKq16FkR…
2026-05-24 08:44:09     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:44:09     Fetched 20 texts (20 indices)
2026-05-24 08:44:09    Downloading
2026-05-24 08:44:09 andrebarrosilva1123/evolai-mamba2-c@dc37c985d66c77e3d10bf9eaf16e6dc952c62e17…
2026-05-24 08:44:11     Loaded (local prefetch)
2026-05-24 08:44:11     Model 0.48B → batch=512, seq=16384
2026-05-24 08:44:12    Ready:
2026-05-24 08:44:12 andrebarrosilva1123/evolai-mamba2-c@dc37c985d66c77e3d10bf9eaf16e6dc952c62e17
2026-05-24 08:44:15     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 08:44:15     Loss 4.9396 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 08:44:15 0.0000 | KL 4.9396 | NextKL 4.8183 | SideQ 0% | Score 0.0000 (3.9s)
2026-05-24 08:44:15     Gate FAIL | Improve seed/ref mismatch cur=4.9396 req<=0.0000 prev=mismatch |
2026-05-24 08:44:15 Consist ok ema_cur=4.7705 ema_next=4.7693 ratio=1.000 max<=1.20
2026-05-24 08:44:17   Evicted cached model:
2026-05-24 08:44:17 clear-blue-sky/evolai-reborn-tfm-005@4e2c98f78611b6f2e63d6baad12b51c589f8afb3
2026-05-24 08:44:17   [11/15] UID 11 | Lin2es/evolai-mb2-01v @
2026-05-24 08:44:17 a7f32e5ce7f8d307c98560e5025525f3703310c0 | hotkey 5HYuS4jrJJ56…
2026-05-24 08:44:17     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:44:17    Downloading
2026-05-24 08:44:17 evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a…
2026-05-24 08:44:17     Fetched 20 texts (20 indices)
2026-05-24 08:44:18    emission scale=1.000 (active miners)
2026-05-24 08:44:19    emission scale=1.000 (active miners)
2026-05-24 08:44:19    all quality scores zero after gates — emission share redistributed to
2026-05-24 08:44:19 productive tracks
2026-05-24 08:44:19     Loaded (local prefetch)
2026-05-24 08:44:19     Model 0.48B → batch=512, seq=16384
2026-05-24 08:44:21    Ready: evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a
2026-05-24 08:44:22   ✓  set at 08:44:22 UTC
2026-05-24 08:44:23     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 08:44:23     Loss 4.6542 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 08:44:23 0.1465 | KL 4.6542 | NextKL 4.6361 | SideQ 0% | Score 0.0000 (3.6s)
2026-05-24 08:44:23     Gate FAIL | Improve seed/ref mismatch cur=4.6542 req<=0.0000 prev=mismatch |
2026-05-24 08:44:23 Consist ok ema_cur=4.6515 ema_next=4.6594 ratio=1.002 max<=1.20
2026-05-24 08:44:25   Evicted cached model:
2026-05-24 08:44:25 Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4
2026-05-24 08:44:25   [12/15] UID 58 | andrebarrosilva1123/evolai-mamba2-c @
2026-05-24 08:44:25 dc37c985d66c77e3d10bf9eaf16e6dc952c62e17 | hotkey 5EgtSzXJbjpV…
2026-05-24 08:44:25     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:44:25    Downloading
2026-05-24 08:44:25 Radiant28/evolai-mamba2-0.47b-v2@475bf7bf65af1192ed824d58816c1d83f3475983…
2026-05-24 08:44:25     Fetched 20 texts (20 indices)
2026-05-24 08:44:27     Loaded (local prefetch)
2026-05-24 08:44:27     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 08:44:28    Ready:
2026-05-24 08:44:28 Radiant28/evolai-mamba2-0.47b-v2@475bf7bf65af1192ed824d58816c1d83f3475983
2026-05-24 08:44:29   [13/15] UID 96 | evolai/evolai_mamba_naive_kl @
2026-05-24 08:44:29 b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a | hotkey 5HQuJVXBXGrW…
2026-05-24 08:44:29     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:44:29     Fetched 20 texts (20 indices)
2026-05-24 08:44:29    Downloading
2026-05-24 08:44:29 batster4/evolai-mamba2-v1@142f14d218be618e3161d86926085b3a9cefed55…
2026-05-24 08:44:30     Loaded (local prefetch)
2026-05-24 08:44:30     Model 0.46B → batch=512, seq=16384
2026-05-24 08:44:32    Ready: batster4/evolai-mamba2-v1@142f14d218be618e3161d86926085b3a9cefed55
2026-05-24 08:44:38     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:05
2026-05-24 08:44:39     Loss 3.5728 | Size ×0.50 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 08:44:39 0.0000 | KL 3.5728 | NextKL 3.5533 | SideQ 0% | Score 0.0000 (8.3s)
2026-05-24 08:44:39     Gate FAIL | Improve seed/ref mismatch cur=3.5728 req<=0.0000 prev=mismatch |
2026-05-24 08:44:39 Consist ok ema_cur=4.0780 ema_next=3.5055 ratio=0.860 max<=1.20
2026-05-24 08:44:40   Evicted cached model:
2026-05-24 08:44:40 clear-blue-sky/evolai-reborn-tfm-008@47961a2955038f307126b383cedfcaf3c83fc00e
2026-05-24 08:44:41   [14/15] UID 39 | Radiant28/evolai-mamba2-0.47b-v2 @
2026-05-24 08:44:41 475bf7bf65af1192ed824d58816c1d83f3475983 | hotkey 5FvTt3gVVhFT…
2026-05-24 08:44:41     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:44:41     Fetched 20 texts (20 indices)
2026-05-24 08:44:42     Loaded (local prefetch)
2026-05-24 08:44:43     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 08:44:44   [15/15] UID 60 | batster4/evolai-mamba2-v1 @
2026-05-24 08:44:44 142f14d218be618e3161d86926085b3a9cefed55 | hotkey 5Dc8EpAixcqc…
2026-05-24 08:44:44     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:44:44     Fetched 20 texts (20 indices)
2026-05-24 08:44:46     Loaded (local prefetch)
2026-05-24 08:44:46     ⚠ Invalid model size (0.82B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 08:44:48   Cached next refs for mamba2: 15 miner(s)
2026-05-24 08:44:48 
2026-05-24 08:44:48   ✓ MAMBA2: 7 evaluated, 14 skipped — epoch_22924_mamba2_20260524_081230.json
2026-05-24 08:44:48   ✓ Telemetry sent (7 records)
2026-05-24 08:44:48 Current Leaderboard:
2026-05-24 08:45:03 
2026-05-24 08:45:03 TRANSFORMER
2026-05-24 08:45:03 ┏━━━━━━┳━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━━━┳━━━━━━━┓
2026-05-24 08:45:03 ┃      ┃     ┃        ┃     Latest ┃           ┃       ┃     ┃         ┃       ┃
2026-05-24 08:45:03 ┃ Rank ┃ UID ┃  Score ┃       Loss ┃ ThinkGain ┃  Flow ┃ SQ% ┃      KL ┃ Evals ┃
2026-05-24 08:45:03 ┡━━━━━━╇━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━━━╇━━━━━━━┩
2026-05-24 08:45:03 │    1 │  87 │ 0.0000 │     4.0577 │  0 FAIL   │ 0.133 │  0% │  2.2495 │   147 │
2026-05-24 08:45:03 │    2 │  86 │ 0.0000 │     4.1094 │  0 FAIL   │ 0.139 │  0% │  2.3171 │   148 │
2026-05-24 08:45:03 │    3 │   8 │ 0.0000 │     3.6027 │  0 FAIL   │ 0.017 │  0% │  1.7487 │   307 │
2026-05-24 08:45:03 │    4 │   9 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 08:45:03 │    5 │  25 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   343 │
2026-05-24 08:45:03 │    6 │  33 │ 0.0000 │     2.8796 │  0 FAIL   │ 0.042 │  0% │  2.2918 │   344 │
2026-05-24 08:45:03 │    7 │  35 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 08:45:03 │    8 │  36 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   343 │
2026-05-24 08:45:03 │    9 │  37 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 08:45:03 │   10 │  38 │ 0.0000 │     2.8907 │  0 FAIL   │ 0.245 │  0% │  2.2559 │   343 │
2026-05-24 08:45:03 │   11 │  40 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 08:45:03 │   12 │  42 │ 0.0000 │     2.9319 │  0 FAIL   │ 0.189 │  0% │  2.4191 │   344 │
2026-05-24 08:45:03 │   13 │  43 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 08:45:03 │   14 │  44 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 08:45:03 │   15 │  45 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 08:45:03 │   16 │  48 │ 0.0000 │     4.1999 │  0 FAIL   │ 0.000 │  0% │  2.3440 │   131 │
2026-05-24 08:45:03 │   17 │  49 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   343 │
2026-05-24 08:45:03 │   18 │  50 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   343 │
2026-05-24 08:45:03 │   19 │  51 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   316 │
2026-05-24 08:45:03 │   20 │  52 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   317 │
2026-05-24 08:45:03 │   21 │  53 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 08:45:03 │   22 │  54 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   315 │
2026-05-24 08:45:03 │   23 │  55 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 08:45:03 │   24 │  59 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 08:45:03 │   25 │  61 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 08:45:03 │   26 │  62 │ 0.0000 │     4.0717 │  0 FAIL   │ 0.000 │  0% │  2.0717 │   344 │
2026-05-24 08:45:03 │   27 │  65 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 08:45:03 │   28 │  66 │ 0.0000 │     3.9005 │  0 FAIL   │ 0.000 │  0% │  2.0171 │   342 │
2026-05-24 08:45:03 │   29 │  67 │ 0.0000 │     3.6892 │  0 FAIL   │ 0.457 │  0% │  1.8500 │   344 │
2026-05-24 08:45:03 │   30 │  69 │ 0.0000 │     3.9368 │  0 FAIL   │ 0.260 │  0% │  2.0164 │   127 │
2026-05-24 08:45:03 │   31 │  70 │ 0.0000 │     4.0898 │  0 FAIL   │ 0.000 │  0% │  1.9655 │   342 │
2026-05-24 08:45:03 │   32 │  72 │ 0.0000 │     3.5856 │  0 FAIL   │ 0.000 │  0% │  1.9312 │   126 │
2026-05-24 08:45:03 │   33 │  73 │ 0.0000 │     3.8153 │  0 FAIL   │ 0.000 │  0% │  1.8722 │   127 │
2026-05-24 08:45:03 │   34 │  75 │ 0.0000 │     2.9821 │  0 FAIL   │ 0.261 │  0% │  2.2377 │   345 │
2026-05-24 08:45:03 │   35 │  76 │ 0.0000 │     2.8645 │  0 FAIL   │ 0.000 │  0% │  2.7470 │   343 │
2026-05-24 08:45:03 │   36 │  77 │ 0.0000 │     2.8218 │  0 FAIL   │ 0.000 │  0% │  2.7014 │   246 │
2026-05-24 08:45:03 │   37 │  78 │ 0.0000 │     2.9082 │  0 FAIL   │ 0.000 │  0% │  2.8450 │   246 │
2026-05-24 08:45:03 │   38 │  79 │ 0.0000 │     2.2274 │  0 FAIL   │ 0.157 │  0% │  2.3798 │   246 │
2026-05-24 08:45:03 │   39 │  80 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 08:45:03 │   40 │  82 │ 0.0000 │     3.7075 │  0 FAIL   │ 0.190 │  0% │  1.6882 │   342 │
2026-05-24 08:45:03 │   41 │  83 │ 0.0000 │     3.7473 │  0 FAIL   │ 0.000 │  0% │  1.9585 │   344 │
2026-05-24 08:45:03 │   42 │  84 │ 0.0000 │     3.7714 │  0 FAIL   │ 0.000 │  0% │  1.8660 │   328 │
2026-05-24 08:45:03 │   43 │  85 │ 0.0000 │     3.8056 │  0 FAIL   │ 0.000 │  0% │  1.9754 │   331 │
2026-05-24 08:45:03 │   44 │  88 │ 0.0000 │     3.9147 │  0 FAIL   │ 0.290 │  0% │  1.9992 │   146 │
2026-05-24 08:45:03 │   45 │  92 │ 0.0000 │     2.9164 │  0 FAIL   │ 0.000 │  0% │  2.4377 │   247 │
2026-05-24 08:45:03 │   46 │  93 │ 0.0000 │     3.8102 │  0 FAIL   │ 0.017 │  0% │  1.9333 │   127 │
2026-05-24 08:45:03 │   47 │  94 │ 0.0000 │     3.7989 │  0 FAIL   │ 0.000 │  0% │  1.7722 │   257 │
2026-05-24 08:45:03 │   48 │  95 │ 0.0000 │     2.5799 │  0 FAIL   │ 0.017 │  0% │  2.8590 │   256 │
2026-05-24 08:45:03 │   49 │  97 │ 0.0000 │     3.9830 │  0 FAIL   │ 0.000 │  0% │  1.8816 │   257 │
2026-05-24 08:45:03 │   50 │  98 │ 0.0000 │     3.8961 │  0 FAIL   │ 0.139 │  0% │  2.0310 │   256 │
2026-05-24 08:45:03 │   51 │  99 │ 0.0000 │     4.2079 │  0 FAIL   │ 0.000 │  0% │  2.0532 │   125 │
2026-05-24 08:45:03 │   52 │ 100 │ 0.0000 │     4.1601 │  0 FAIL   │ 0.000 │  0% │  4.1897 │   255 │
2026-05-24 08:45:03 │   53 │ 101 │ 0.0000 │     3.8400 │  0 FAIL   │ 0.227 │  0% │  1.8151 │    77 │
2026-05-24 08:45:03 └──────┴─────┴────────┴────────────┴───────────┴───────┴─────┴─────────┴───────┘
2026-05-24 08:45:03 
2026-05-24 08:45:03 MAMBA2
2026-05-24 08:45:03 ┏━━━━━━┳━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━━━┳━━━━━━━┓
2026-05-24 08:45:03 ┃      ┃     ┃        ┃     Latest ┃           ┃       ┃     ┃         ┃       ┃
2026-05-24 08:45:03 ┃ Rank ┃ UID ┃  Score ┃       Loss ┃ ThinkGain ┃  Flow ┃ SQ% ┃      KL ┃ Evals ┃
2026-05-24 08:45:03 ┡━━━━━━╇━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━━━╇━━━━━━━┩
2026-05-24 08:45:03 │    1 │  11 │ 0.0000 │     4.6542 │  0 FAIL   │ 0.147 │  0% │  4.6542 │   246 │
2026-05-24 08:45:03 │    2 │  30 │ 0.0000 │     4.7515 │  0 FAIL   │ 0.228 │  0% │  4.7515 │   341 │
2026-05-24 08:45:03 │    3 │  31 │ 0.0000 │     4.9396 │  0 FAIL   │ 0.000 │  0% │  4.9396 │   341 │
2026-05-24 08:45:03 │    4 │  32 │ 0.0000 │     5.0221 │  0 FAIL   │ 0.000 │  0% │  5.0221 │   341 │
2026-05-24 08:45:03 │    5 │  34 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   341 │
2026-05-24 08:45:03 │    6 │  39 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   342 │
2026-05-24 08:45:03 │    7 │  41 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   341 │
2026-05-24 08:45:03 │    8 │  56 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   341 │
2026-05-24 08:45:03 │    9 │  57 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   341 │
2026-05-24 08:45:03 │   10 │  58 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   341 │
2026-05-24 08:45:03 │   11 │  60 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   341 │
2026-05-24 08:45:03 │   12 │  63 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   271 │
2026-05-24 08:45:03 │   13 │  64 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 08:45:03 │   14 │  68 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 08:45:03 │   15 │  71 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   271 │
2026-05-24 08:45:03 │   16 │  74 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 08:45:03 │   17 │  81 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   273 │
2026-05-24 08:45:03 │   18 │  89 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   246 │
2026-05-24 08:45:03 │   19 │  90 │ 0.0000 │     4.6753 │  0 FAIL   │ 0.000 │  0% │  4.6753 │   256 │
2026-05-24 08:45:03 │   20 │  91 │ 0.0000 │     4.6669 │  0 FAIL   │ 0.007 │  0% │  4.6669 │   256 │
2026-05-24 08:45:03 │   21 │  96 │ 0.0000 │     3.5728 │  0 FAIL   │ 0.000 │  0% │  3.5728 │   256 │
2026-05-24 08:45:03 └──────┴─────┴────────┴────────────┴───────────┴───────┴─────┴─────────┴───────┘
2026-05-24 08:45:03 
2026-05-24 08:45:03 Round complete in epoch 22924 (1953s elapsed). Starting next round immediately…
2026-05-24 08:45:03 
2026-05-24 08:45:03 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2026-05-24 08:45:03 
2026-05-24 08:45:03 ━━━ Epoch #22924 (Loop #2) ━━━ block=8252836, ~32m remaining
2026-05-24 08:45:12 
2026-05-24 08:45:12   ⚠ UID 86: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:45:12 (Request ID:
2026-05-24 08:45:12 Root=1-6a12ba98-7ce4abf5064676b56cf71bd1;39cd6986-d4fc-469c-b743-d9b232722460)
2026-05-24 08:45:12 
2026-05-24 08:45:12 Repository Not Found for url:
2026-05-24 08:45:12 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-012/revision/main.
2026-05-24 08:45:12 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:45:12 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:45:12 authenticated and your token has the required permissions.
2026-05-24 08:45:12 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:45:12 Invalid username or password.
2026-05-24 08:45:12   ⚠ UID 87: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:45:12 (Request ID:
2026-05-24 08:45:12 Root=1-6a12ba98-03846ed66b108e533f2891ee;963453cf-5452-4729-bda9-0b60b2413b9a)
2026-05-24 08:45:12 
2026-05-24 08:45:12 Repository Not Found for url:
2026-05-24 08:45:12 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-013/revision/main.
2026-05-24 08:45:12 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:45:12 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:45:12 authenticated and your token has the required permissions.
2026-05-24 08:45:12 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:45:12 Invalid username or password.
2026-05-24 08:45:12   ⚠ UID 88: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:45:12 (Request ID:
2026-05-24 08:45:12 Root=1-6a12ba98-455b9c11241abdbf2ad00320;45c257b1-8c5b-438d-be66-009c4fa139d2)
2026-05-24 08:45:12 
2026-05-24 08:45:12 Repository Not Found for url:
2026-05-24 08:45:12 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-014/revision/main.
2026-05-24 08:45:12 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:45:12 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:45:12 authenticated and your token has the required permissions.
2026-05-24 08:45:12 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:45:12 Invalid username or password.
2026-05-24 08:45:13   Locked transformer revisions (50 miner(s), 3 skipped)
2026-05-24 08:45:21   ⚠ UID 63: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:45:21 (Request ID:
2026-05-24 08:45:21 Root=1-6a12baa1-579c1dda4f428eed56bd56bb;c33b922f-1303-4a5c-a144-3b8f51a2d1e0)
2026-05-24 08:45:21 
2026-05-24 08:45:21 Repository Not Found for url:
2026-05-24 08:45:21 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-009/revision/main.
2026-05-24 08:45:21 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:45:21 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:45:21 authenticated and your token has the required permissions.
2026-05-24 08:45:21 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:45:21 Invalid username or password.
2026-05-24 08:45:21   ⚠ UID 64: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:45:21 (Request ID:
2026-05-24 08:45:21 Root=1-6a12baa1-2141cb02222ce41e02c7f6b7;51c36563-eb38-4426-b861-18f8c064b684)
2026-05-24 08:45:21 
2026-05-24 08:45:21 Repository Not Found for url:
2026-05-24 08:45:21 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-002/revision/main.
2026-05-24 08:45:21 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:45:21 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:45:21 authenticated and your token has the required permissions.
2026-05-24 08:45:21 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:45:21 Invalid username or password.
2026-05-24 08:45:21   ⚠ UID 68: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:45:21 (Request ID:
2026-05-24 08:45:21 Root=1-6a12baa1-2eabc91371f8caed42bf40af;2fccc530-9efb-40e8-94d0-bd056273aa63)
2026-05-24 08:45:21 
2026-05-24 08:45:21 Repository Not Found for url:
2026-05-24 08:45:21 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-008/revision/main.
2026-05-24 08:45:21 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:45:21 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:45:21 authenticated and your token has the required permissions.
2026-05-24 08:45:21 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:45:21 Invalid username or password.
2026-05-24 08:45:21   ⚠ UID 71: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:45:21 (Request ID:
2026-05-24 08:45:21 Root=1-6a12baa1-2d59f6344f01aaa836ffb765;99525388-ad00-4659-9bec-5e124ba4d8e4)
2026-05-24 08:45:21 
2026-05-24 08:45:21 Repository Not Found for url:
2026-05-24 08:45:21 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-001/revision/main.
2026-05-24 08:45:21 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:45:21 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:45:21 authenticated and your token has the required permissions.
2026-05-24 08:45:21 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:45:21 Invalid username or password.
2026-05-24 08:45:21   ⚠ UID 74: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:45:21 (Request ID:
2026-05-24 08:45:21 Root=1-6a12baa1-1aae221d060827563fb608cb;ed92f1fb-0841-4633-8e03-3b8b195756d9)
2026-05-24 08:45:21 
2026-05-24 08:45:21 Repository Not Found for url:
2026-05-24 08:45:21 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-007/revision/main.
2026-05-24 08:45:21 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:45:21 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:45:21 authenticated and your token has the required permissions.
2026-05-24 08:45:21 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:45:21 Invalid username or password.
2026-05-24 08:45:21   ⚠ UID 81: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 08:45:21 (Request ID:
2026-05-24 08:45:21 Root=1-6a12baa1-1ed9b625699393716421366b;902e286e-ca2f-4b1c-9e90-262d861cabc7)
2026-05-24 08:45:21 
2026-05-24 08:45:21 Repository Not Found for url:
2026-05-24 08:45:21 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-010/revision/main.
2026-05-24 08:45:21 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 08:45:21 If you are trying to access a private or gated repo, make sure you are
2026-05-24 08:45:21 authenticated and your token has the required permissions.
2026-05-24 08:45:21 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 08:45:21 Invalid username or password.
2026-05-24 08:45:21   Locked mamba2 revisions (15 miner(s), 6 skipped)
2026-05-24 08:45:50   Committed round seed epoch=22924 seed=ee0803ae...
2026-05-24 08:45:51 Evaluating TRANSFORMER track…
2026-05-24 08:45:51 
2026-05-24 08:45:51   Found 50 locked transformer miners
2026-05-24 08:45:51    Downloading
2026-05-24 08:45:51 andrebarrosilva1123/evolai-b@3414c0abb8793ed4af56fd5e6e536b8b0f5ac520…
2026-05-24 08:45:51 Pre-building current/next challenges for 50 miners…
2026-05-24 08:45:51 Fetching 7 files: 100%|██████████| 7/7 [00:06<00:00,  1.13it/s]
2026-05-24 08:45:57    Ready: andrebarrosilva1123/evolai-b@3414c0abb8793ed4af56fd5e6e536b8b0f5ac520
2026-05-24 08:45:57    Downloading
2026-05-24 08:45:57 logosnodos/evolai-qwen-1.5b@7e121e8efe6c6b93d622e9a53972d221e763d10b…
2026-05-24 08:45:57 Fetching 17 files: 100%|██████████| 17/17 [00:43<00:00,  2.54s/it]
2026-05-24 08:46:40    Ready: logosnodos/evolai-qwen-1.5b@7e121e8efe6c6b93d622e9a53972d221e763d10b
2026-05-24 08:46:59 ✓ Ref data ready: submitted=50, cached=50
2026-05-24 08:46:59   [1/50] UID 50 | andrebarrosilva1123/evolai-b @
2026-05-24 08:46:59 3414c0abb8793ed4af56fd5e6e536b8b0f5ac520 | hotkey 5FXELcBK4WiD…
2026-05-24 08:46:59     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:46:59     Fetched 20 texts (20 indices)
2026-05-24 08:46:59    Downloading
2026-05-24 08:46:59 andrebarrosilva1123/evolai-0.4b@fa913c93aa7a7449066ce870427387bd3fc7e841…
2026-05-24 08:47:02     Loaded (local prefetch)
2026-05-24 08:47:03     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:47:06   [2/50] UID 61 | logosnodos/evolai-qwen-1.5b @
2026-05-24 08:47:06 7e121e8efe6c6b93d622e9a53972d221e763d10b | hotkey 5FNTU6ZYgKup…
2026-05-24 08:47:06     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:47:06     Fetched 20 texts (20 indices)
2026-05-24 08:47:06    Ready:
2026-05-24 08:47:06 andrebarrosilva1123/evolai-0.4b@fa913c93aa7a7449066ce870427387bd3fc7e841
2026-05-24 08:47:06    Downloading
2026-05-24 08:47:06 mrthor102/evolai-tfm-super-003@75d4671ce2bf769be9ded4bd4205abef791212d1…
2026-05-24 08:47:09     Loaded (local prefetch)
2026-05-24 08:47:11    Ready:
2026-05-24 08:47:11 mrthor102/evolai-tfm-super-003@75d4671ce2bf769be9ded4bd4205abef791212d1
2026-05-24 08:47:14     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:47:16   [3/50] UID 49 | andrebarrosilva1123/evolai-0.4b @
2026-05-24 08:47:16 fa913c93aa7a7449066ce870427387bd3fc7e841 | hotkey 5DULz3AJEisH…
2026-05-24 08:47:16     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:47:16    Downloading
2026-05-24 08:47:16 clear-blue-sky/evolai-reborn-tfm-011@3c6fb9eda1f125661a5c6e9f4243ace37e38e4b5…
2026-05-24 08:47:16     Fetched 20 texts (20 indices)
2026-05-24 08:47:18     Loaded (local prefetch)
2026-05-24 08:47:18     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:47:20   [4/50] UID 98 | mrthor102/evolai-tfm-super-003 @
2026-05-24 08:47:20 75d4671ce2bf769be9ded4bd4205abef791212d1 | hotkey 5Hgy59m2Hzm1…
2026-05-24 08:47:20     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:47:20     Fetched 20 texts (20 indices)
2026-05-24 08:47:20    Ready:
2026-05-24 08:47:20 clear-blue-sky/evolai-reborn-tfm-011@3c6fb9eda1f125661a5c6e9f4243ace37e38e4b5
2026-05-24 08:47:20    Downloading
2026-05-24 08:47:20 Radiant28/evolai-transformer-0.4b-b2@808b61992e043ca99ff5b412a6cf61bfbb3fd793…
2026-05-24 08:47:22     Loaded (local prefetch)
2026-05-24 08:47:23     Model 0.46B → batch=512, seq=16384
2026-05-24 08:47:27    Ready:
2026-05-24 08:47:27 Radiant28/evolai-transformer-0.4b-b2@808b61992e043ca99ff5b412a6cf61bfbb3fd793
2026-05-24 08:48:23     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:56
2026-05-24 08:48:24     Loss 4.0897 | Size ×0.50 | Think 4.0897 | ThinkGain 0 (+0.4602) | Flow
2026-05-24 08:48:24 0.0292 | KL 2.0044 | NextKL 1.8700 | SideQ 0% | Score 0.0000 (59.9s)
2026-05-24 08:48:24     Gate FAIL | Improve FAIL cur=2.0044 req<=1.9675 prev=2.0076 | Consist ok
2026-05-24 08:48:24 ema_cur=1.9158 ema_next=1.9090 ratio=0.996 max<=1.20
2026-05-24 08:48:25   Evicted cached model:
2026-05-24 08:48:25 Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8
2026-05-24 08:48:26   [5/50] UID 73 | clear-blue-sky/evolai-reborn-tfm-011 @
2026-05-24 08:48:26 3c6fb9eda1f125661a5c6e9f4243ace37e38e4b5 | hotkey 5CSAM6rnGRPk…
2026-05-24 08:48:26     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:48:26     Fetched 20 texts (20 indices)
2026-05-24 08:48:26    Downloading
2026-05-24 08:48:26 mrthor102/evolai-tfm-super-002@db9483fdd7fb46c99ba8731900ec009330f4e77e…
2026-05-24 08:48:28     Loaded (local prefetch)
2026-05-24 08:48:28     Model 0.46B → batch=512, seq=16384
2026-05-24 08:48:31    Ready:
2026-05-24 08:48:31 mrthor102/evolai-tfm-super-002@db9483fdd7fb46c99ba8731900ec009330f4e77e
2026-05-24 08:49:32     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:58
2026-05-24 08:49:32     Loss 3.6379 | Size ×0.50 | Think 3.6379 | ThinkGain 0 (+0.4633) | Flow
2026-05-24 08:49:32 0.0000 | KL 1.8415 | NextKL 1.7976 | SideQ 0% | Score 0.0000 (63.6s)
2026-05-24 08:49:32     Gate FAIL | Improve FAIL cur=1.8415 req<=1.8081 prev=1.8450 | Consist ok
2026-05-24 08:49:32 ema_cur=2.5145 ema_next=1.8549 ratio=0.738 max<=1.20
2026-05-24 08:49:34   Evicted cached model:
2026-05-24 08:49:34 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c
2026-05-24 08:49:34   [6/50] UID 37 | Radiant28/evolai-transformer-0.4b-b2 @
2026-05-24 08:49:34 808b61992e043ca99ff5b412a6cf61bfbb3fd793 | hotkey 5HjbzF3e9waA…
2026-05-24 08:49:34     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:49:34     Fetched 20 texts (20 indices)
2026-05-24 08:49:34    Downloading
2026-05-24 08:49:34 mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c…
2026-05-24 08:49:37     Loaded (local prefetch)
2026-05-24 08:49:37     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:49:39   [7/50] UID 97 | mrthor102/evolai-tfm-super-002 @
2026-05-24 08:49:39 db9483fdd7fb46c99ba8731900ec009330f4e77e | hotkey 5EcJYRJBVF5K…
2026-05-24 08:49:39     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:49:39     Fetched 20 texts (20 indices)
2026-05-24 08:49:39    Ready: mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c
2026-05-24 08:49:39    Downloading
2026-05-24 08:49:39 mrthor102/evolai-tfm-super-001@c2dac74023c984bf5261f93f33f748659f16f224…
2026-05-24 08:49:41     Loaded (local prefetch)
2026-05-24 08:49:42     Model 0.46B → batch=512, seq=16384
2026-05-24 08:49:44    Ready:
2026-05-24 08:49:44 mrthor102/evolai-tfm-super-001@c2dac74023c984bf5261f93f33f748659f16f224
2026-05-24 08:50:46     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:01:00
2026-05-24 08:50:46     Loss 3.7542 | Size ×0.50 | Think 3.7542 | ThinkGain 0 (+0.4622) | Flow
2026-05-24 08:50:46 0.0000 | KL 1.9200 | NextKL 2.0417 | SideQ 0% | Score 0.0000 (63.4s)
2026-05-24 08:50:46     Gate FAIL | Improve FAIL cur=1.9200 req<=1.8786 prev=1.9169 | Consist ok
2026-05-24 08:50:46 ema_cur=1.9308 ema_next=1.9394 ratio=1.004 max<=1.20
2026-05-24 08:50:47   Evicted cached model:
2026-05-24 08:50:47 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518
2026-05-24 08:50:49   [8/50] UID 33 | mihai-777/evolai-tfm-1p5b @
2026-05-24 08:50:49 594894f806fb4c014675d89aad14f1c68976d52c | hotkey 5F22JM4of6TR…
2026-05-24 08:50:49     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:50:49     Fetched 20 texts (20 indices)
2026-05-24 08:50:49    Downloading snx999/evolai_qw_4b@69eff663b4e9a2b5bf76dde6cdecc5dce29759d3…
2026-05-24 08:50:50     Loaded (local prefetch)
2026-05-24 08:50:50     Model 0.46B → batch=512, seq=16384
2026-05-24 08:51:04    Ready: snx999/evolai_qw_4b@69eff663b4e9a2b5bf76dde6cdecc5dce29759d3
2026-05-24 08:51:53     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:59
2026-05-24 08:51:53     Loss 3.2509 | Size ×0.50 | Think 3.2509 | ThinkGain 0 (+0.4518) | Flow
2026-05-24 08:51:53 0.0000 | KL 2.5351 | NextKL 2.2523 | SideQ 0% | Score 0.0000 (62.5s)
2026-05-24 08:51:53     Gate FAIL | Improve same SHA cur=2.5351 req<=2.4844 prev=2.5351 | Consist ok
2026-05-24 08:51:53 ema_cur=2.4147 ema_next=2.4167 ratio=1.001 max<=1.20
2026-05-24 08:51:55   Evicted cached model:
2026-05-24 08:51:55 Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd
2026-05-24 08:51:55   [9/50] UID 94 | mrthor102/evolai-tfm-super-001 @
2026-05-24 08:51:55 c2dac74023c984bf5261f93f33f748659f16f224 | hotkey 5CPXihPMoGQ2…
2026-05-24 08:51:55     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:51:55     Fetched 20 texts (20 indices)
2026-05-24 08:51:55    Downloading
2026-05-24 08:51:55 Radiant28/evolai-transformer-0.4b-b0@7a08a8009fa8b8f82d1ad0febc442a89020082d1…
2026-05-24 08:51:57     Loaded (local prefetch)
2026-05-24 08:51:57     Model 0.46B → batch=512, seq=16384
2026-05-24 08:52:02    Ready:
2026-05-24 08:52:02 Radiant28/evolai-transformer-0.4b-b0@7a08a8009fa8b8f82d1ad0febc442a89020082d1
2026-05-24 08:52:49     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:48
2026-05-24 08:52:49     Loss 4.0320 | Size ×0.50 | Think 4.0320 | ThinkGain 0 (+0.4580) | Flow
2026-05-24 08:52:49 0.0000 | KL 1.9489 | NextKL 1.6471 | SideQ 0% | Score 0.0000 (51.3s)
2026-05-24 08:52:49     Gate FAIL | Improve FAIL cur=1.9489 req<=1.9145 prev=1.9535 | Consist ok
2026-05-24 08:52:49 ema_cur=1.9290 ema_next=1.9137 ratio=0.992 max<=1.20
2026-05-24 08:52:51   Evicted cached model:
2026-05-24 08:52:51 mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7
2026-05-24 08:52:51   [10/50] UID 25 | snx999/evolai_qw_4b @
2026-05-24 08:52:51 69eff663b4e9a2b5bf76dde6cdecc5dce29759d3 | hotkey 5HBJoNWv4nAi…
2026-05-24 08:52:51     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:52:51     Fetched 20 texts (20 indices)
2026-05-24 08:52:51    Downloading
2026-05-24 08:52:51 clear-blue-sky/evolai-reborn-tfm-002@9d512cab2a9007b7d58a6ec4988e6ac869910be5…
2026-05-24 08:52:54     Loaded (local prefetch)
2026-05-24 08:52:55     ⚠ Invalid model size (4.21B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 08:52:56    Ready:
2026-05-24 08:52:56 clear-blue-sky/evolai-reborn-tfm-002@9d512cab2a9007b7d58a6ec4988e6ac869910be5
2026-05-24 08:52:57   [11/50] UID 45 | Radiant28/evolai-transformer-0.4b-b0 @
2026-05-24 08:52:57 7a08a8009fa8b8f82d1ad0febc442a89020082d1 | hotkey 5F1B3j7EyjuE…
2026-05-24 08:52:57     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:52:57     Fetched 20 texts (20 indices)
2026-05-24 08:52:57    Downloading
2026-05-24 08:52:57 clear-blue-sky/evolai-reborn-tfm-010@a925485d558b5b141050fd8bc943880e4a97b289…
2026-05-24 08:53:00     Loaded (local prefetch)
2026-05-24 08:53:00     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:53:02    Ready:
2026-05-24 08:53:02 clear-blue-sky/evolai-reborn-tfm-010@a925485d558b5b141050fd8bc943880e4a97b289
2026-05-24 08:53:02   [12/50] UID 67 | clear-blue-sky/evolai-reborn-tfm-002 @
2026-05-24 08:53:02 9d512cab2a9007b7d58a6ec4988e6ac869910be5 | hotkey 5GC7k2mkTKGF…
2026-05-24 08:53:02     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:53:02     Fetched 20 texts (20 indices)
2026-05-24 08:53:02    Downloading
2026-05-24 08:53:02 mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678…
2026-05-24 08:53:04     Loaded (local prefetch)
2026-05-24 08:53:04     Model 0.46B → batch=512, seq=16384
2026-05-24 08:53:06    Ready: mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678
2026-05-24 08:53:39     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:32
2026-05-24 08:53:39     Loss 3.8033 | Size ×0.50 | Think 3.8033 | ThinkGain 0 (+0.4583) | Flow
2026-05-24 08:53:39 0.3830 | KL 1.9292 | NextKL 1.8789 | SideQ 0% | Score 0.0000 (34.8s)
2026-05-24 08:53:39     Gate FAIL | Improve FAIL cur=1.9292 req<=1.8782 prev=1.9166 | Consist ok
2026-05-24 08:53:39 ema_cur=1.8951 ema_next=1.8928 ratio=0.999 max<=1.20
2026-05-24 08:53:40   Evicted cached model:
2026-05-24 08:53:40 Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0
2026-05-24 08:53:41   [13/50] UID 72 | clear-blue-sky/evolai-reborn-tfm-010 @
2026-05-24 08:53:41 a925485d558b5b141050fd8bc943880e4a97b289 | hotkey 5H3rMcqJQcbK…
2026-05-24 08:53:41    Downloading
2026-05-24 08:53:41 mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a…
2026-05-24 08:53:41     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:53:41     Fetched 20 texts (20 indices)
2026-05-24 08:53:42     Loaded (local prefetch)
2026-05-24 08:53:42     Model 0.46B → batch=512, seq=16384
2026-05-24 08:53:45    Ready: mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a
2026-05-24 08:54:16     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:31
2026-05-24 08:54:16     Loss 3.6976 | Size ×0.50 | Think 3.6976 | ThinkGain 0 (+0.4594) | Flow
2026-05-24 08:54:16 0.1863 | KL 1.6246 | NextKL 1.9608 | SideQ 0% | Score 0.0000 (33.7s)
2026-05-24 08:54:16     Gate FAIL | Improve FAIL cur=1.6246 req<=1.5829 prev=1.6153 | Consist ok
2026-05-24 08:54:16 ema_cur=1.8791 ema_next=1.9057 ratio=1.014 max<=1.20
2026-05-24 08:54:18   Evicted cached model:
2026-05-24 08:54:18 evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a
2026-05-24 08:54:18   [14/50] UID 42 | mihai-777/evolai-tfm-1p5b-v5 @
2026-05-24 08:54:18 bd42aeb0828dfa0126f7fc825e13b49209fec678 | hotkey 5C5WCYnsrXRz…
2026-05-24 08:54:18     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:54:18     Fetched 20 texts (20 indices)
2026-05-24 08:54:18    Downloading
2026-05-24 08:54:18 andrebarrosilva1123/evolai-e@806394ca7f2f7c1edbe962a9471647f4d67b5e72…
2026-05-24 08:54:20     Loaded (local prefetch)
2026-05-24 08:54:20     Model 0.46B → batch=512, seq=16384
2026-05-24 08:54:24    Ready: andrebarrosilva1123/evolai-e@806394ca7f2f7c1edbe962a9471647f4d67b5e72
2026-05-24 08:54:58     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 08:54:58     Loss 3.1897 | Size ×0.50 | Think 3.1897 | ThinkGain 0 (+0.4566) | Flow
2026-05-24 08:54:58 0.1673 | KL 2.4519 | NextKL 2.3318 | SideQ 0% | Score 0.0000 (38.1s)
2026-05-24 08:54:58     Gate FAIL | Improve same SHA cur=2.4519 req<=2.4029 prev=2.4519 | Consist ok
2026-05-24 08:54:58 ema_cur=2.4372 ema_next=2.4395 ratio=1.001 max<=1.20
2026-05-24 08:55:00   Evicted cached model:
2026-05-24 08:55:00 mrthor102/evolai-tfm-super-003@75d4671ce2bf769be9ded4bd4205abef791212d1
2026-05-24 08:55:00   [15/50] UID 75 | mihai-777/evolai-tfm-1p5b-04 @
2026-05-24 08:55:00 fb289dbfe35c595b1a586f786a19e118cc1bfc9a | hotkey 5Dnz76SAsEv8…
2026-05-24 08:55:00     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:55:00     Fetched 20 texts (20 indices)
2026-05-24 08:55:00    Downloading
2026-05-24 08:55:00 clear-blue-sky/evolai-reborn-tfm-006@8c0b26d62d13ade4af1eaeea5967245266f27921…
2026-05-24 08:55:02     Loaded (local prefetch)
2026-05-24 08:55:02     Model 0.46B → batch=512, seq=16384
2026-05-24 08:55:04    Ready:
2026-05-24 08:55:04 clear-blue-sky/evolai-reborn-tfm-006@8c0b26d62d13ade4af1eaeea5967245266f27921
2026-05-24 08:55:40     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 08:55:41     Loss 2.8941 | Size ×0.50 | Think 2.8941 | ThinkGain 0 (+0.4499) | Flow
2026-05-24 08:55:41 0.2925 | KL 2.2630 | NextKL 2.3897 | SideQ 0% | Score 0.0000 (38.3s)
2026-05-24 08:55:41     Gate FAIL | Improve same SHA cur=2.2630 req<=2.2178 prev=2.2630 | Consist ok
2026-05-24 08:55:41 ema_cur=2.3335 ema_next=2.3563 ratio=1.010 max<=1.20
2026-05-24 08:55:42   Evicted cached model:
2026-05-24 08:55:42 clear-blue-sky/evolai-reborn-tfm-011@3c6fb9eda1f125661a5c6e9f4243ace37e38e4b5
2026-05-24 08:55:43   [16/50] UID 53 | andrebarrosilva1123/evolai-e @
2026-05-24 08:55:43 806394ca7f2f7c1edbe962a9471647f4d67b5e72 | hotkey 5EFgFa93M5Vx…
2026-05-24 08:55:43     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:55:43     Fetched 20 texts (20 indices)
2026-05-24 08:55:43    Downloading
2026-05-24 08:55:43 Radiant28/evolai-transformer-0.4b-b1@18231d7d50096d8b2744fdff1b38a7b90246ddf0…
2026-05-24 08:55:45     Loaded (local prefetch)
2026-05-24 08:55:45     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:55:48   [17/50] UID 66 | clear-blue-sky/evolai-reborn-tfm-006 @
2026-05-24 08:55:48 8c0b26d62d13ade4af1eaeea5967245266f27921 | hotkey 5E4M4B5sVED5…
2026-05-24 08:55:48     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:55:48     Fetched 20 texts (20 indices)
2026-05-24 08:55:49    Ready:
2026-05-24 08:55:49 Radiant28/evolai-transformer-0.4b-b1@18231d7d50096d8b2744fdff1b38a7b90246ddf0
2026-05-24 08:55:49    Downloading
2026-05-24 08:55:49 clear-blue-sky/evolai-reborn-tfm-007@75e0277bd4a5c60cc06a210fa9d5a05561356ef9…
2026-05-24 08:55:49     Loaded (local prefetch)
2026-05-24 08:55:49 Fetching 7 files: 100%|██████████| 7/7 [00:04<00:00,  1.62it/s]
2026-05-24 08:55:50     Model 0.46B → batch=512, seq=16384
2026-05-24 08:55:54    Ready:
2026-05-24 08:55:54 clear-blue-sky/evolai-reborn-tfm-007@75e0277bd4a5c60cc06a210fa9d5a05561356ef9
2026-05-24 08:56:28     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 08:56:28     Loss 3.7772 | Size ×0.50 | Think 3.7772 | ThinkGain 0 (+0.4617) | Flow
2026-05-24 08:56:28 0.0000 | KL 1.9541 | NextKL 2.1556 | SideQ 0% | Score 0.0000 (38.0s)
2026-05-24 08:56:28     Gate FAIL | Improve FAIL cur=1.9541 req<=1.9109 prev=1.9499 | Consist ok
2026-05-24 08:56:28 ema_cur=1.9678 ema_next=1.9804 ratio=1.006 max<=1.20
2026-05-24 08:56:29   Evicted cached model:
2026-05-24 08:56:29 mrthor102/evolai-tfm-super-002@db9483fdd7fb46c99ba8731900ec009330f4e77e
2026-05-24 08:56:30   [18/50] UID 35 | Radiant28/evolai-transformer-0.4b-b1 @
2026-05-24 08:56:30 18231d7d50096d8b2744fdff1b38a7b90246ddf0 | hotkey 5EXZBq3wQzTK…
2026-05-24 08:56:30     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:56:30     Fetched 20 texts (20 indices)
2026-05-24 08:56:30    Downloading Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600…
2026-05-24 08:56:32     Loaded (local prefetch)
2026-05-24 08:56:32    Ready: Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600
2026-05-24 08:56:33     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:56:34   [19/50] UID 84 | clear-blue-sky/evolai-reborn-tfm-007 @
2026-05-24 08:56:34 75e0277bd4a5c60cc06a210fa9d5a05561356ef9 | hotkey 5H1DaT8Dtt4N…
2026-05-24 08:56:34     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:56:34     Fetched 20 texts (20 indices)
2026-05-24 08:56:34    Downloading
2026-05-24 08:56:34 clear-blue-sky/evolai-reborn-tfm-003@8ec7e0ac5234f745104d4288bc15caf873d6a618…
2026-05-24 08:56:36     Loaded (local prefetch)
2026-05-24 08:56:36     Model 0.46B → batch=512, seq=16384
2026-05-24 08:56:38    Ready:
2026-05-24 08:56:38 clear-blue-sky/evolai-reborn-tfm-003@8ec7e0ac5234f745104d4288bc15caf873d6a618
2026-05-24 08:57:14     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 08:57:15     Loss 3.9665 | Size ×0.50 | Think 3.9665 | ThinkGain 0 (+0.4611) | Flow
2026-05-24 08:57:15 0.0000 | KL 1.8725 | NextKL 1.9723 | SideQ 0% | Score 0.0000 (38.0s)
2026-05-24 08:57:15     Gate FAIL | Improve FAIL cur=1.8725 req<=1.8331 prev=1.8705 | Consist ok
2026-05-24 08:57:15 ema_cur=1.9446 ema_next=1.9687 ratio=1.012 max<=1.20
2026-05-24 08:57:16   Evicted cached model:
2026-05-24 08:57:16 mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c
2026-05-24 08:57:17   [20/50] UID 79 | Lin2es/evolai-tfm-03o @
2026-05-24 08:57:17 2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600 | hotkey 5D4eNqXRjWmX…
2026-05-24 08:57:17     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:57:17     Fetched 20 texts (20 indices)
2026-05-24 08:57:17    Downloading
2026-05-24 08:57:17 mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba…
2026-05-24 08:57:18     Loaded (local prefetch)
2026-05-24 08:57:18     Model 0.46B → batch=512, seq=16384
2026-05-24 08:57:21    Ready: mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba
2026-05-24 08:57:56     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 08:57:57     Loss 2.3688 | Size ×0.50 | Think 2.3688 | ThinkGain 0 (+0.4574) | Flow
2026-05-24 08:57:57 0.0017 | KL 2.6815 | NextKL 2.7448 | SideQ 0% | Score 0.0000 (38.1s)
2026-05-24 08:57:57     Gate FAIL | Improve same SHA cur=2.6815 req<=2.6279 prev=2.6815 | Consist ok
2026-05-24 08:57:57 ema_cur=2.4307 ema_next=2.4653 ratio=1.014 max<=1.20
2026-05-24 08:57:58   Evicted cached model:
2026-05-24 08:57:58 mrthor102/evolai-tfm-super-001@c2dac74023c984bf5261f93f33f748659f16f224
2026-05-24 08:57:59   [21/50] UID 82 | clear-blue-sky/evolai-reborn-tfm-003 @
2026-05-24 08:57:59 8ec7e0ac5234f745104d4288bc15caf873d6a618 | hotkey 5EtDxpyqHywK…
2026-05-24 08:57:59     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:57:59     Fetched 20 texts (20 indices)
2026-05-24 08:57:59    Downloading
2026-05-24 08:57:59 dreamiii0406/evolai-0p47b-v1@fea2659bdf8bd35e5382c50e4857f1ab20f20262…
2026-05-24 08:58:00     Loaded (local prefetch)
2026-05-24 08:58:01     Model 0.46B → batch=512, seq=16384
2026-05-24 08:58:02    Ready: dreamiii0406/evolai-0p47b-v1@fea2659bdf8bd35e5382c50e4857f1ab20f20262
2026-05-24 08:58:38     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 08:58:39     Loss 3.8200 | Size ×0.50 | Think 3.8200 | ThinkGain 0 (+0.4594) | Flow
2026-05-24 08:58:39 0.2167 | KL 1.8514 | NextKL 1.7884 | SideQ 0% | Score 0.0000 (37.9s)
2026-05-24 08:58:39     Gate FAIL | Improve FAIL cur=1.8514 req<=1.8042 prev=1.8410 | Consist ok
2026-05-24 08:58:39 ema_cur=1.8892 ema_next=1.9045 ratio=1.008 max<=1.20
2026-05-24 08:58:40   Evicted cached model:
2026-05-24 08:58:40 clear-blue-sky/evolai-reborn-tfm-002@9d512cab2a9007b7d58a6ec4988e6ac869910be5
2026-05-24 08:58:41   [22/50] UID 76 | mihai-777/evolai-tfm-1p5b-05 @
2026-05-24 08:58:41 a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba | hotkey 5GLBxPtoiB7R…
2026-05-24 08:58:41     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:58:41     Fetched 20 texts (20 indices)
2026-05-24 08:58:41    Downloading Radiant28/evolai-1p5b@e351598db6d77f85b5081768df04d37c132750f0…
2026-05-24 08:58:42     Loaded (local prefetch)
2026-05-24 08:58:42     Model 0.46B → batch=512, seq=16384
2026-05-24 08:58:48    Ready: Radiant28/evolai-1p5b@e351598db6d77f85b5081768df04d37c132750f0
2026-05-24 08:59:18     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:33
2026-05-24 08:59:19     Loss 2.7042 | Size ×0.50 | Think 2.7042 | ThinkGain 0 (+0.4533) | Flow
2026-05-24 08:59:19 0.0381 | KL 1.9994 | NextKL 2.4729 | SideQ 0% | Score 0.0000 (36.0s)
2026-05-24 08:59:19     Gate FAIL | Improve same SHA cur=1.9994 req<=1.9594 prev=1.9994 | Consist ok
2026-05-24 08:59:19 ema_cur=2.4487 ema_next=2.4337 ratio=0.994 max<=1.20
2026-05-24 08:59:20   Evicted cached model:
2026-05-24 08:59:20 clear-blue-sky/evolai-reborn-tfm-010@a925485d558b5b141050fd8bc943880e4a97b289
2026-05-24 08:59:21   [23/50] UID 80 | dreamiii0406/evolai-0p47b-v1 @
2026-05-24 08:59:21 fea2659bdf8bd35e5382c50e4857f1ab20f20262 | hotkey 5Cd2zZyMQnvp…
2026-05-24 08:59:21     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:59:21     Fetched 20 texts (20 indices)
2026-05-24 08:59:21    Downloading
2026-05-24 08:59:21 mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a…
2026-05-24 08:59:22     Loaded (local prefetch)
2026-05-24 08:59:22     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:59:24   [24/50] UID 43 | Radiant28/evolai-1p5b @
2026-05-24 08:59:24 e351598db6d77f85b5081768df04d37c132750f0 | hotkey 5HSz4knZnWHY…
2026-05-24 08:59:24     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:59:24     Fetched 20 texts (20 indices)
2026-05-24 08:59:24    Ready: mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a
2026-05-24 08:59:24    Downloading
2026-05-24 08:59:24 mrthor102/evolai-tfm-super-004@6623560efa96f6a92a6b9557dcf0e2b1ae0391cc…
2026-05-24 08:59:26     Loaded (local prefetch)
2026-05-24 08:59:26     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 08:59:28   [25/50] UID 38 | mihai-777/evolai-tfm-1p5b-alt @
2026-05-24 08:59:28 5ebb4a406916abe39e32823ff1f635b70e707e5a | hotkey 5FbfiXysyCtC…
2026-05-24 08:59:28     Challenge: evolai/universal_qa(20 idx)
2026-05-24 08:59:28     Fetched 20 texts (20 indices)
2026-05-24 08:59:28    Ready:
2026-05-24 08:59:28 mrthor102/evolai-tfm-super-004@6623560efa96f6a92a6b9557dcf0e2b1ae0391cc
2026-05-24 08:59:28    Downloading
2026-05-24 08:59:28 Radiant28/evolai-0.4b-V1@5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5…
2026-05-24 08:59:30     Loaded (local prefetch)
2026-05-24 08:59:30     Model 0.46B → batch=512, seq=16384
2026-05-24 08:59:35    Ready: Radiant28/evolai-0.4b-V1@5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5
2026-05-24 09:00:08     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:00:08     Loss 3.3598 | Size ×0.50 | Think 3.3598 | ThinkGain 0 (+0.4531) | Flow
2026-05-24 09:00:08 0.1984 | KL 2.4190 | NextKL 2.4928 | SideQ 0% | Score 0.0000 (38.3s)
2026-05-24 09:00:08     Gate FAIL | Improve same SHA cur=2.4190 req<=2.3706 prev=2.4190 | Consist ok
2026-05-24 09:00:08 ema_cur=2.3721 ema_next=2.4020 ratio=1.013 max<=1.20
2026-05-24 09:00:10   Evicted cached model:
2026-05-24 09:00:10 mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678
2026-05-24 09:00:11   [26/50] UID 99 | mrthor102/evolai-tfm-super-004 @
2026-05-24 09:00:11 6623560efa96f6a92a6b9557dcf0e2b1ae0391cc | hotkey 5EnuPuwNaqmP…
2026-05-24 09:00:11     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:00:11    Downloading evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4…
2026-05-24 09:00:11     Fetched 20 texts (20 indices)
2026-05-24 09:00:12     Loaded (local prefetch)
2026-05-24 09:00:13     Model 0.46B → batch=512, seq=16384
2026-05-24 09:00:13    Ready: evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4
2026-05-24 09:00:50     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 09:00:50     Loss 4.0723 | Size ×0.50 | Think 4.0723 | ThinkGain 0 (+0.4593) | Flow
2026-05-24 09:00:50 0.0000 | KL 1.9656 | NextKL 2.0584 | SideQ 0% | Score 0.0000 (37.3s)
2026-05-24 09:00:50     Gate FAIL | Improve FAIL cur=1.9656 req<=1.9398 prev=1.9794 | Consist ok
2026-05-24 09:00:50 ema_cur=1.9589 ema_next=1.9643 ratio=1.003 max<=1.20
2026-05-24 09:00:51   Evicted cached model:
2026-05-24 09:00:51 mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a
2026-05-24 09:00:52   [27/50] UID 44 | Radiant28/evolai-0.4b-V1 @
2026-05-24 09:00:52 5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5 | hotkey 5DXm2ShZGmwG…
2026-05-24 09:00:52    Downloading philk11/evolai-0.4b@822950352d63cdd145c3a7449ebfd4b51ad5ae6a…
2026-05-24 09:00:52     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:00:52     Fetched 20 texts (20 indices)
2026-05-24 09:00:54     Loaded (local prefetch)
2026-05-24 09:00:54     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:00:55    Ready: philk11/evolai-0.4b@822950352d63cdd145c3a7449ebfd4b51ad5ae6a
2026-05-24 09:00:56   [28/50] UID 95 | evolai/evolai_naive_kl @
2026-05-24 09:00:56 da8203b6900f14ec1b724f3dd8c6dc35576fc3e4 | hotkey 5CXwmm7R4U6o…
2026-05-24 09:00:56     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:00:56     Fetched 20 texts (20 indices)
2026-05-24 09:00:56    Downloading
2026-05-24 09:00:56 Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9…
2026-05-24 09:00:58     Loaded (local prefetch)
2026-05-24 09:00:58     Model 0.46B → batch=512, seq=16384
2026-05-24 09:01:01    Ready: Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9
2026-05-24 09:01:37     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:01:37     Loss 3.1120 | Size ×0.50 | Think 3.1120 | ThinkGain 0 (+0.4841) | Flow
2026-05-24 09:01:37 0.0842 | KL 2.6833 | NextKL 2.7039 | SideQ 0% | Score 0.0000 (38.9s)
2026-05-24 09:01:37     Gate FAIL | Improve same SHA cur=2.6833 req<=2.6296 prev=2.6833 | Consist ok
2026-05-24 09:01:37 ema_cur=2.8463 ema_next=2.8167 ratio=0.990 max<=1.20
2026-05-24 09:01:39   Evicted cached model:
2026-05-24 09:01:39 clear-blue-sky/evolai-reborn-tfm-006@8c0b26d62d13ade4af1eaeea5967245266f27921
2026-05-24 09:01:39   [29/50] UID 65 | philk11/evolai-0.4b @
2026-05-24 09:01:39 822950352d63cdd145c3a7449ebfd4b51ad5ae6a | hotkey 5GvHE1tHbhGv…
2026-05-24 09:01:39     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:01:39     Fetched 20 texts (20 indices)
2026-05-24 09:01:39    Downloading
2026-05-24 09:01:39 andrebarrosilva1123/evolai-f@89654c7b1e351cce36bab65fe09692eb0e109f72…
2026-05-24 09:01:41     Loaded (local prefetch)
2026-05-24 09:01:41     ⚠ Invalid model size (0.60B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 09:01:43   [30/50] UID 93 | Phoenix9781/evolai-tf-model @
2026-05-24 09:01:43 b05038fcfdcc79fa8d8e79730074b65cd68c73f9 | hotkey 5F4R25t78FSF…
2026-05-24 09:01:43     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:01:43     Fetched 20 texts (20 indices)
2026-05-24 09:01:45     Loaded (local prefetch)
2026-05-24 09:01:45     Model 0.46B → batch=512, seq=16384
2026-05-24 09:01:46    Ready: andrebarrosilva1123/evolai-f@89654c7b1e351cce36bab65fe09692eb0e109f72
2026-05-24 09:01:46    Downloading
2026-05-24 09:01:46 clear-blue-sky/evolai-reborn-tfm-004@2921306430562eff35ea2c11aabd1b9412e19961…
2026-05-24 09:01:46 Fetching 7 files: 100%|██████████| 7/7 [00:04<00:00,  1.48it/s]
2026-05-24 09:01:51    Ready:
2026-05-24 09:01:51 clear-blue-sky/evolai-reborn-tfm-004@2921306430562eff35ea2c11aabd1b9412e19961
2026-05-24 09:02:24     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:02:24     Loss 3.9991 | Size ×0.50 | Think 3.9991 | ThinkGain 0 (+0.4585) | Flow
2026-05-24 09:02:24 0.0000 | KL 2.1836 | NextKL 1.9957 | SideQ 0% | Score 0.0000 (38.3s)
2026-05-24 09:02:24     Gate FAIL | Improve same SHA cur=2.1836 req<=2.1399 prev=2.1836 | Consist ok
2026-05-24 09:02:24 ema_cur=1.9736 ema_next=1.9675 ratio=0.997 max<=1.20
2026-05-24 09:02:26   Evicted cached model:
2026-05-24 09:02:26 clear-blue-sky/evolai-reborn-tfm-007@75e0277bd4a5c60cc06a210fa9d5a05561356ef9
2026-05-24 09:02:26   [31/50] UID 52 | andrebarrosilva1123/evolai-f @
2026-05-24 09:02:26 89654c7b1e351cce36bab65fe09692eb0e109f72 | hotkey 5HTZZEb5oxv9…
2026-05-24 09:02:26     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:02:26     Fetched 20 texts (20 indices)
2026-05-24 09:02:26    Downloading
2026-05-24 09:02:26 evolai/evolai_test_challenge@71d0f7058e451a387164d5b4497cda29481578ca…
2026-05-24 09:02:28     Loaded (local prefetch)
2026-05-24 09:02:29     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:02:30    Ready: evolai/evolai_test_challenge@71d0f7058e451a387164d5b4497cda29481578ca
2026-05-24 09:02:31   [32/50] UID 70 | clear-blue-sky/evolai-reborn-tfm-004 @
2026-05-24 09:02:31 2921306430562eff35ea2c11aabd1b9412e19961 | hotkey 5Hdg2gHopWQK…
2026-05-24 09:02:31     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:02:31     Fetched 20 texts (20 indices)
2026-05-24 09:02:31    Downloading
2026-05-24 09:02:31 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb…
2026-05-24 09:02:32     Loaded (local prefetch)
2026-05-24 09:02:33     Model 0.46B → batch=512, seq=16384
2026-05-24 09:02:35    Ready:
2026-05-24 09:02:35 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb
2026-05-24 09:03:11     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:03:11     Loss 4.0522 | Size ×0.50 | Think 4.0522 | ThinkGain 0 (+0.4658) | Flow
2026-05-24 09:03:11 0.0000 | KL 1.9079 | NextKL 1.9566 | SideQ 0% | Score 0.0000 (38.5s)
2026-05-24 09:03:11     Gate FAIL | Improve FAIL cur=1.9079 req<=1.8775 prev=1.9158 | Consist ok
2026-05-24 09:03:11 ema_cur=1.9035 ema_next=1.9107 ratio=1.004 max<=1.20
2026-05-24 09:03:13   Evicted cached model:
2026-05-24 09:03:13 Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600
2026-05-24 09:03:14   [33/50] UID 8 | evolai/evolai_test_challenge @
2026-05-24 09:03:14 71d0f7058e451a387164d5b4497cda29481578ca | hotkey 5ENhqnBoyFdz…
2026-05-24 09:03:14     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:03:14     Fetched 20 texts (20 indices)
2026-05-24 09:03:14    Downloading
2026-05-24 09:03:14 Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002…
2026-05-24 09:03:15     Loaded (local prefetch)
2026-05-24 09:03:16     Model 0.46B → batch=512, seq=16384
2026-05-24 09:03:17    Ready: Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002
2026-05-24 09:03:51     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:33
2026-05-24 09:03:52     Loss 3.8917 | Size ×0.50 | Think 3.8917 | ThinkGain 0 (+0.4525) | Flow
2026-05-24 09:03:52 0.0000 | KL 1.7940 | NextKL 2.0210 | SideQ 0% | Score 0.0310 (35.8s)
2026-05-24 09:03:52     Gate PASS | Improve ok cur=1.7940 req<=1.9240 prev=1.9632 | Consist ok
2026-05-24 09:03:52 ema_cur=1.7366 ema_next=1.9529 ratio=1.125 max<=1.20
2026-05-24 09:03:53   Evicted cached model:
2026-05-24 09:03:53 clear-blue-sky/evolai-reborn-tfm-003@8ec7e0ac5234f745104d4288bc15caf873d6a618
2026-05-24 09:03:53   [34/50] UID 48 | sangerno63/evolai-transformer-v2 @
2026-05-24 09:03:53 4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb | hotkey 5ED3KNj5uEVS…
2026-05-24 09:03:53     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:03:53     Fetched 20 texts (20 indices)
2026-05-24 09:03:53    Downloading Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d…
2026-05-24 09:03:55     Loaded (local prefetch)
2026-05-24 09:03:55     Model 0.46B → batch=512, seq=16384
2026-05-24 09:03:56    Ready: Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d
2026-05-24 09:04:33     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 09:04:33     Loss 3.8975 | Size ×0.50 | Think 3.8975 | ThinkGain 0 (+0.4418) | Flow
2026-05-24 09:04:33 0.1655 | KL 1.9501 | NextKL 2.2343 | SideQ 0% | Score 0.0000 (37.6s)
2026-05-24 09:04:33     Gate FAIL | Improve same SHA cur=1.9501 req<=1.9111 prev=1.9501 | Consist ok
2026-05-24 09:04:33 ema_cur=2.1894 ema_next=2.1854 ratio=0.998 max<=1.20
2026-05-24 09:04:35   Evicted cached model:
2026-05-24 09:04:35 mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba
2026-05-24 09:04:35   [35/50] UID 100 | Danieli1021/evolai-qwen047-v3 @
2026-05-24 09:04:35 e01dfd3b9c54325c98bf12966bdebadace391002 | hotkey 5DMH2VrrukYd…
2026-05-24 09:04:35     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:04:35     Fetched 20 texts (20 indices)
2026-05-24 09:04:35    Downloading galuis116/evolai-future@7591e0441945f1ba85f2e78d6239cee711a66dce…
2026-05-24 09:04:37     Loaded (local prefetch)
2026-05-24 09:04:37     Model 0.47B → batch=512, seq=16384
2026-05-24 09:04:40    Ready: galuis116/evolai-future@7591e0441945f1ba85f2e78d6239cee711a66dce
2026-05-24 09:04:58     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:17
2026-05-24 09:04:58     Loss 4.0175 | Size ×0.51 | Think 4.0175 | ThinkGain 0 (+0.4807) | Flow
2026-05-24 09:04:58 0.0000 | KL 3.8966 | NextKL 3.8850 | SideQ 0% | Score 0.0000 (20.6s)
2026-05-24 09:04:58     Gate FAIL | Improve same SHA cur=3.8966 req<=3.8187 prev=3.8966 | Consist ok
2026-05-24 09:04:58 ema_cur=4.4474 ema_next=3.9321 ratio=0.884 max<=1.20
2026-05-24 09:04:59   Evicted cached model:
2026-05-24 09:04:59 mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a
2026-05-24 09:05:00   [36/50] UID 77 | Lin2es/evolai-tfm-01o @
2026-05-24 09:05:00 d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d | hotkey 5GQydjNVEhMb…
2026-05-24 09:05:00     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:05:00    Downloading
2026-05-24 09:05:00 clear-blue-sky/evolai-reborn-tfm-009@8e9182e3c2d2a51341f6b7ad8f9f9b4c9405ae24…
2026-05-24 09:05:00     Fetched 20 texts (20 indices)
2026-05-24 09:05:01     Loaded (local prefetch)
2026-05-24 09:05:02     Model 0.46B → batch=512, seq=16384
2026-05-24 09:05:04    Ready:
2026-05-24 09:05:04 clear-blue-sky/evolai-reborn-tfm-009@8e9182e3c2d2a51341f6b7ad8f9f9b4c9405ae24
2026-05-24 09:05:40     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:05:40     Loss 2.1734 | Size ×0.50 | Think 2.1734 | ThinkGain 0 (+0.4360) | Flow
2026-05-24 09:05:40 0.0000 | KL 2.3550 | NextKL 2.3210 | SideQ 0% | Score 0.0000 (38.3s)
2026-05-24 09:05:40     Gate FAIL | Improve same SHA cur=2.3550 req<=2.3079 prev=2.3550 | Consist ok
2026-05-24 09:05:40 ema_cur=2.6228 ema_next=2.5727 ratio=0.981 max<=1.20
2026-05-24 09:05:42   Evicted cached model:
2026-05-24 09:05:42 mrthor102/evolai-tfm-super-004@6623560efa96f6a92a6b9557dcf0e2b1ae0391cc
2026-05-24 09:05:42   [37/50] UID 101 | galuis116/evolai-future @
2026-05-24 09:05:42 7591e0441945f1ba85f2e78d6239cee711a66dce | hotkey 5DPz76uobJLT…
2026-05-24 09:05:42     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:05:42     Fetched 20 texts (20 indices)
2026-05-24 09:05:42    Downloading
2026-05-24 09:05:42 andrebarrosilva1123/evolai-d@89649e9376dace64f631711d3d270198e376702e…
2026-05-24 09:05:44     Loaded (local prefetch)
2026-05-24 09:05:44     Model 0.46B → batch=512, seq=16384
2026-05-24 09:05:48    Ready: andrebarrosilva1123/evolai-d@89649e9376dace64f631711d3d270198e376702e
2026-05-24 09:06:22     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:06:22     Loss 3.6719 | Size ×0.50 | Think 3.6719 | ThinkGain 0 (+0.4599) | Flow
2026-05-24 09:06:22 0.3271 | KL 1.7446 | NextKL 1.6579 | SideQ 0% | Score 0.0000 (37.8s)
2026-05-24 09:06:22     Gate FAIL | Improve FAIL cur=1.7446 req<=1.6958 prev=1.7305 | Consist ok
2026-05-24 09:06:22 ema_cur=1.8919 ema_next=1.8683 ratio=0.988 max<=1.20
2026-05-24 09:06:24   Evicted cached model:
2026-05-24 09:06:24 evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4
2026-05-24 09:06:24   [38/50] UID 69 | clear-blue-sky/evolai-reborn-tfm-009 @
2026-05-24 09:06:24 8e9182e3c2d2a51341f6b7ad8f9f9b4c9405ae24 | hotkey 5ChUCf3NjrgS…
2026-05-24 09:06:24     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:06:24     Fetched 20 texts (20 indices)
2026-05-24 09:06:24    Downloading
2026-05-24 09:06:24 andrebarrosilva1123/evolai-c@6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c…
2026-05-24 09:06:26     Loaded (local prefetch)
2026-05-24 09:06:26     Model 0.46B → batch=512, seq=16384
2026-05-24 09:06:31    Ready: andrebarrosilva1123/evolai-c@6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c
2026-05-24 09:07:05     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 09:07:05     Loss 3.4968 | Size ×0.50 | Think 3.4968 | ThinkGain 0 (+0.4603) | Flow
2026-05-24 09:07:05 0.3849 | KL 1.6931 | NextKL 1.8861 | SideQ 0% | Score 0.0000 (39.0s)
2026-05-24 09:07:05     Gate FAIL | Improve FAIL cur=1.6931 req<=1.6478 prev=1.6814 | Consist ok
2026-05-24 09:07:05 ema_cur=1.9015 ema_next=1.9045 ratio=1.002 max<=1.20
2026-05-24 09:07:07   Evicted cached model:
2026-05-24 09:07:07 Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9
2026-05-24 09:07:08   [39/50] UID 51 | andrebarrosilva1123/evolai-d @
2026-05-24 09:07:08 89649e9376dace64f631711d3d270198e376702e | hotkey 5EhLiPB1GHwH…
2026-05-24 09:07:08     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:07:08     Fetched 20 texts (20 indices)
2026-05-24 09:07:08    Downloading
2026-05-24 09:07:08 Roystar/evolai-qwen2.5-1.5b@47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1…
2026-05-24 09:07:10     Loaded (local prefetch)
2026-05-24 09:07:10     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:07:12   [40/50] UID 54 | andrebarrosilva1123/evolai-c @
2026-05-24 09:07:12 6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c | hotkey 5D7HPRR2QdDB…
2026-05-24 09:07:12     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:07:12     Fetched 20 texts (20 indices)
2026-05-24 09:07:14    Ready: Roystar/evolai-qwen2.5-1.5b@47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1
2026-05-24 09:07:14    Downloading Jubilant/evolai-1.54b@d8681d30b14cb5a597d2ff7c909998cf9d217599…
2026-05-24 09:07:14     Loaded (local prefetch)
2026-05-24 09:07:14 Fetching 7 files: 100%|██████████| 7/7 [00:06<00:00,  1.15it/s]
2026-05-24 09:07:15     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:07:17   [41/50] UID 55 | Roystar/evolai-qwen2.5-1.5b @
2026-05-24 09:07:17 47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1 | hotkey 5DhRJtUeVA6P…
2026-05-24 09:07:17     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:07:17     Fetched 20 texts (20 indices)
2026-05-24 09:07:19     Loaded (local prefetch)
2026-05-24 09:07:19     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:07:20    Ready: Jubilant/evolai-1.54b@d8681d30b14cb5a597d2ff7c909998cf9d217599
2026-05-24 09:07:20    Downloading Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59…
2026-05-24 09:07:22   [42/50] UID 36 | Jubilant/evolai-1.54b @
2026-05-24 09:07:22 d8681d30b14cb5a597d2ff7c909998cf9d217599 | hotkey 5G7Co5VNfQio…
2026-05-24 09:07:22     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:07:22     Fetched 20 texts (20 indices)
2026-05-24 09:07:22 Fetching 7 files: 100%|██████████| 7/7 [00:02<00:00,  2.48it/s]
2026-05-24 09:07:24     Loaded (local prefetch)
2026-05-24 09:07:24     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:07:25    Ready: Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59
2026-05-24 09:07:25    Downloading
2026-05-24 09:07:25 clear-blue-sky/evolai-reborn-tfm-001@5233a721363395c7abfdcfad299f43520b003100…
2026-05-24 09:07:25 Fetching 7 files: 100%|██████████| 7/7 [00:04<00:00,  1.50it/s]
2026-05-24 09:07:26   [43/50] UID 78 | Lin2es/evolai-tfm-02o @
2026-05-24 09:07:26 fc5fc3ee4a3877b825b404dc85c9367c1f248c59 | hotkey 5FA2kgLNs36d…
2026-05-24 09:07:26     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:07:26     Fetched 20 texts (20 indices)
2026-05-24 09:07:28     Loaded (local prefetch)
2026-05-24 09:07:28     Model 0.46B → batch=512, seq=16384
2026-05-24 09:07:30    Ready:
2026-05-24 09:07:30 clear-blue-sky/evolai-reborn-tfm-001@5233a721363395c7abfdcfad299f43520b003100
2026-05-24 09:07:30    Downloading
2026-05-24 09:07:30 Jubilant/evolai-1.50b-v1@074810c41bab77c52a216e0c2f7886484e12deeb…
2026-05-24 09:07:30 Fetching 7 files: 100%|██████████| 7/7 [00:05<00:00,  1.31it/s]
2026-05-24 09:07:35    Ready: Jubilant/evolai-1.50b-v1@074810c41bab77c52a216e0c2f7886484e12deeb
2026-05-24 09:08:06     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 76/76 100% 0:00:35
2026-05-24 09:08:06     Loss 2.6394 | Size ×0.50 | Think 2.6394 | ThinkGain 0 (+0.4268) | Flow
2026-05-24 09:08:06 0.0000 | KL 2.8060 | NextKL 2.5967 | SideQ 0% | Score 0.0000 (38.3s)
2026-05-24 09:08:06     Gate FAIL | Improve same SHA cur=2.8060 req<=2.7499 prev=2.8060 | Consist ok
2026-05-24 09:08:06 ema_cur=2.8079 ema_next=2.7834 ratio=0.991 max<=1.20
2026-05-24 09:08:08   Evicted cached model:
2026-05-24 09:08:08 clear-blue-sky/evolai-reborn-tfm-004@2921306430562eff35ea2c11aabd1b9412e19961
2026-05-24 09:08:08   [44/50] UID 62 | clear-blue-sky/evolai-reborn-tfm-001 @
2026-05-24 09:08:08 5233a721363395c7abfdcfad299f43520b003100 | hotkey 5EjjVuNJsjqP…
2026-05-24 09:08:08     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:08:08     Fetched 20 texts (20 indices)
2026-05-24 09:08:08    Downloading
2026-05-24 09:08:08 dexserbia/evolai-gemma2-9b@7fe66309a3847239a4da5b712477f2105e88399b…
2026-05-24 09:08:10     Loaded (local prefetch)
2026-05-24 09:08:10     Model 0.46B → batch=512, seq=16384
2026-05-24 09:08:37    Ready: dexserbia/evolai-gemma2-9b@7fe66309a3847239a4da5b712477f2105e88399b
2026-05-24 09:08:51     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:37
2026-05-24 09:08:51     Loss 3.8803 | Size ×0.50 | Think 3.8803 | ThinkGain 0 (+0.4618) | Flow
2026-05-24 09:08:51 0.0000 | KL 1.8842 | NextKL 1.9640 | SideQ 0% | Score 0.0000 (40.5s)
2026-05-24 09:08:51     Gate FAIL | Improve FAIL cur=1.8842 req<=1.8382 prev=1.8757 | Consist ok
2026-05-24 09:08:51 ema_cur=1.9464 ema_next=1.9279 ratio=0.990 max<=1.20
2026-05-24 09:08:53   Evicted cached model:
2026-05-24 09:08:53 evolai/evolai_test_challenge@71d0f7058e451a387164d5b4497cda29481578ca
2026-05-24 09:08:53   [45/50] UID 40 | Jubilant/evolai-1.50b-v1 @
2026-05-24 09:08:53 074810c41bab77c52a216e0c2f7886484e12deeb | hotkey 5Fuv43yR7tjJ…
2026-05-24 09:08:53     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:08:53     Fetched 20 texts (20 indices)
2026-05-24 09:08:53    Downloading
2026-05-24 09:08:53 clear-blue-sky/evolai-reborn-tfm-005@455b69e426e6ca0721b3f69943223fe21173d569…
2026-05-24 09:08:55     Loaded (local prefetch)
2026-05-24 09:08:56     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:08:58   [46/50] UID 9 | dexserbia/evolai-gemma2-9b @
2026-05-24 09:08:58 7fe66309a3847239a4da5b712477f2105e88399b | hotkey 5EbpxBkVKVNV…
2026-05-24 09:08:58     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:08:58     Fetched 20 texts (20 indices)
2026-05-24 09:08:58    Ready:
2026-05-24 09:08:58 clear-blue-sky/evolai-reborn-tfm-005@455b69e426e6ca0721b3f69943223fe21173d569
2026-05-24 09:08:58    Downloading Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4…
2026-05-24 09:09:00    Ready: Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4
2026-05-24 09:09:03     Loaded (local prefetch)
2026-05-24 09:09:05     ⚠ Invalid model size (9.24B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 09:09:07   [47/50] UID 83 | clear-blue-sky/evolai-reborn-tfm-005 @
2026-05-24 09:09:07 455b69e426e6ca0721b3f69943223fe21173d569 | hotkey 5G8tRiKdn5cC…
2026-05-24 09:09:07     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:09:07    Downloading
2026-05-24 09:09:07 batster4/evolai-phi4-mini-dpo-v1@8217794abaf74f8e15f578a507e27b5f9b1df4c9…
2026-05-24 09:09:07     Fetched 20 texts (20 indices)
2026-05-24 09:09:08     Loaded (local prefetch)
2026-05-24 09:09:09     Model 0.46B → batch=512, seq=16384
2026-05-24 09:09:21    Ready:
2026-05-24 09:09:21 batster4/evolai-phi4-mini-dpo-v1@8217794abaf74f8e15f578a507e27b5f9b1df4c9
2026-05-24 09:09:48     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 09:09:48     Loss 3.8881 | Size ×0.50 | Think 3.8881 | ThinkGain 0 (+0.4622) | Flow
2026-05-24 09:09:48 0.0000 | KL 1.8725 | NextKL 2.0068 | SideQ 0% | Score 0.0000 (39.3s)
2026-05-24 09:09:48     Gate FAIL | Improve FAIL cur=1.8725 req<=1.8249 prev=1.8621 | Consist ok
2026-05-24 09:09:48 ema_cur=2.5994 ema_next=1.9463 ratio=0.749 max<=1.20
2026-05-24 09:09:50   Evicted cached model:
2026-05-24 09:09:50 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb
2026-05-24 09:09:50   [48/50] UID 92 | Lin2es/evolai-tfm-04o @
2026-05-24 09:09:50 52061d203723fdc8be09324d0c827898fcb7bdc4 | hotkey 5GefYX69KUVQ…
2026-05-24 09:09:50     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:09:50     Fetched 20 texts (20 indices)
2026-05-24 09:09:50    Downloading
2026-05-24 09:09:50 clear-blue-sky/evolai-reborn-tfm-008@819b51083eb5f5e01d1a1e50c836daf868e0f1e7…
2026-05-24 09:09:52     Loaded (local prefetch)
2026-05-24 09:09:52     Model 0.46B → batch=512, seq=16384
2026-05-24 09:09:55    Ready:
2026-05-24 09:09:55 clear-blue-sky/evolai-reborn-tfm-008@819b51083eb5f5e01d1a1e50c836daf868e0f1e7
2026-05-24 09:10:30     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:10:30     Loss 2.1641 | Size ×0.50 | Think 2.1641 | ThinkGain 0 (+0.4453) | Flow
2026-05-24 09:10:30 0.0000 | KL 2.1930 | NextKL 2.5771 | SideQ 0% | Score 0.0000 (38.0s)
2026-05-24 09:10:30     Gate FAIL | Improve same SHA cur=2.1930 req<=2.1491 prev=2.1930 | Consist ok
2026-05-24 09:10:30 ema_cur=3.1047 ema_next=2.5273 ratio=0.814 max<=1.20
2026-05-24 09:10:32   Evicted cached model:
2026-05-24 09:10:32 Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002
2026-05-24 09:10:33   [49/50] UID 59 | batster4/evolai-phi4-mini-dpo-v1 @
2026-05-24 09:10:33 8217794abaf74f8e15f578a507e27b5f9b1df4c9 | hotkey 5GCA2s6m4RRM…
2026-05-24 09:10:33     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:10:33     Fetched 20 texts (20 indices)
2026-05-24 09:10:35     Loaded (local prefetch)
2026-05-24 09:10:36     ⚠ Invalid model size (3.84B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 09:10:38   [50/50] UID 85 | clear-blue-sky/evolai-reborn-tfm-008 @
2026-05-24 09:10:38 819b51083eb5f5e01d1a1e50c836daf868e0f1e7 | hotkey 5EC5MzPj6dGb…
2026-05-24 09:10:38     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:10:38     Fetched 20 texts (20 indices)
2026-05-24 09:10:40     Loaded (local prefetch)
2026-05-24 09:10:40     Model 0.46B → batch=512, seq=16384
2026-05-24 09:11:18     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:11:18     Loss 3.9816 | Size ×0.50 | Think 3.9816 | ThinkGain 0 (+0.4618) | Flow
2026-05-24 09:11:18 0.0000 | KL 2.0327 | NextKL 1.8934 | SideQ 0% | Score 0.0000 (37.8s)
2026-05-24 09:11:18     Gate FAIL | Improve FAIL cur=2.0327 req<=1.9834 prev=2.0239 | Consist ok
2026-05-24 09:11:18 ema_cur=2.6031 ema_next=1.9587 ratio=0.752 max<=1.20
2026-05-24 09:11:20   Evicted cached model:
2026-05-24 09:11:20 Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d
2026-05-24 09:11:20   Cached next refs for transformer: 50 miner(s)
2026-05-24 09:11:20 
2026-05-24 09:11:20   ✓ TRANSFORMER: 30 evaluated, 23 skipped —
2026-05-24 09:11:20 epoch_22924_transformer_20260524_084503.json
2026-05-24 09:11:21   ✓ Telemetry sent (30 records)
2026-05-24 09:11:21 Evaluating MAMBA2 track…
2026-05-24 09:11:21 
2026-05-24 09:11:21   Found 15 locked mamba2 miners
2026-05-24 09:11:21    Downloading Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8…
2026-05-24 09:11:21 Pre-building current/next challenges for 15 miners…
2026-05-24 09:11:21 Fetching 7 files: 100%|██████████| 7/7 [00:02<00:00,  2.45it/s]
2026-05-24 09:11:24    Ready: Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8
2026-05-24 09:11:24    Downloading
2026-05-24 09:11:24 elgin-group/evolai-mamba2-0p47b-v1@39b2f90ad08643d34503c88f5c7224fd3dabeed7…
2026-05-24 09:11:25 Fetching 8 files: 100%|██████████| 8/8 [00:03<00:00,  2.38it/s]
2026-05-24 09:11:28    Ready:
2026-05-24 09:11:28 elgin-group/evolai-mamba2-0p47b-v1@39b2f90ad08643d34503c88f5c7224fd3dabeed7
2026-05-24 09:11:41 ✓ Ref data ready: submitted=15, cached=15
2026-05-24 09:11:41   [1/15] UID 90 | Lin2es/evolai-mb2-02v @
2026-05-24 09:11:41 c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8 | hotkey 5CtLLhrw6Lxa…
2026-05-24 09:11:41     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:11:41     Fetched 20 texts (20 indices)
2026-05-24 09:11:41    Downloading
2026-05-24 09:11:41 andrebarrosilva1123/evolai-mamba2-a@55b92d373b1c219a4cfbac7034c154ddbcdc854d…
2026-05-24 09:11:42     Loaded (local prefetch)
2026-05-24 09:11:42     Model 0.48B → batch=512, seq=16384
2026-05-24 09:11:44    Ready:
2026-05-24 09:11:44 andrebarrosilva1123/evolai-mamba2-a@55b92d373b1c219a4cfbac7034c154ddbcdc854d
2026-05-24 09:11:51     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:02
2026-05-24 09:11:52     Loss 4.7356 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:11:52 0.0000 | KL 4.7356 | NextKL 4.6426 | SideQ 0% | Score 0.0000 (8.6s)
2026-05-24 09:11:52     Gate FAIL | Improve same SHA cur=4.7356 req<=4.6409 prev=4.7356 | Consist ok
2026-05-24 09:11:52 ema_cur=5.1434 ema_next=4.7079 ratio=0.915 max<=1.20
2026-05-24 09:11:53   Evicted cached model:
2026-05-24 09:11:53 galuis116/evolai-future@7591e0441945f1ba85f2e78d6239cee711a66dce
2026-05-24 09:11:54   [2/15] UID 34 | elgin-group/evolai-mamba2-0p47b-v1 @
2026-05-24 09:11:54 39b2f90ad08643d34503c88f5c7224fd3dabeed7 | hotkey 5GNJr9NfE9e9…
2026-05-24 09:11:54     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:11:54     Fetched 20 texts (20 indices)
2026-05-24 09:11:54    Downloading
2026-05-24 09:11:54 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c…
2026-05-24 09:11:57    Ready:
2026-05-24 09:11:57 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c
2026-05-24 09:11:57     Loaded (local prefetch)
2026-05-24 09:11:57     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 09:11:59   [3/15] UID 56 | andrebarrosilva1123/evolai-mamba2-a @
2026-05-24 09:11:59 55b92d373b1c219a4cfbac7034c154ddbcdc854d | hotkey 5D1zGn2n3mzF…
2026-05-24 09:11:59     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:11:59     Fetched 20 texts (20 indices)
2026-05-24 09:11:59    Downloading
2026-05-24 09:11:59 andrebarrosilva1123/evolai-mamba2-b@62336a49df6d6014f779575adfd29373c228edd4…
2026-05-24 09:12:03    Ready:
2026-05-24 09:12:03 andrebarrosilva1123/evolai-mamba2-b@62336a49df6d6014f779575adfd29373c228edd4
2026-05-24 09:12:05     Loaded (local prefetch)
2026-05-24 09:12:05     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 09:12:07   [4/15] UID 32 | mihai-777/evolai-mamba2-1p6b-alt @
2026-05-24 09:12:07 131bd3907f9816bbf184f5651ba63af66046e84c | hotkey 5GL84HKDau7C…
2026-05-24 09:12:07     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:12:07     Fetched 20 texts (20 indices)
2026-05-24 09:12:07    Downloading
2026-05-24 09:12:07 Radiant28/evolai-mamba2-0.47b-v3@97f692fb0b295aa29075d3f9d592bfb4e7625b16…
2026-05-24 09:12:09     Loaded (local prefetch)
2026-05-24 09:12:09     Model 0.48B → batch=512, seq=16384
2026-05-24 09:12:10    Ready:
2026-05-24 09:12:10 Radiant28/evolai-mamba2-0.47b-v3@97f692fb0b295aa29075d3f9d592bfb4e7625b16
2026-05-24 09:12:15     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:02
2026-05-24 09:12:15     Loss 4.7938 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:12:15 0.0000 | KL 4.7938 | NextKL 4.8477 | SideQ 0% | Score 0.0000 (5.6s)
2026-05-24 09:12:15     Gate FAIL | Improve same SHA cur=4.7938 req<=4.6979 prev=4.7938 | Consist ok
2026-05-24 09:12:15 ema_cur=4.8881 ema_next=4.8742 ratio=0.997 max<=1.20
2026-05-24 09:12:17   Evicted cached model:
2026-05-24 09:12:17 clear-blue-sky/evolai-reborn-tfm-009@8e9182e3c2d2a51341f6b7ad8f9f9b4c9405ae24
2026-05-24 09:12:17   [5/15] UID 57 | andrebarrosilva1123/evolai-mamba2-b @
2026-05-24 09:12:17 62336a49df6d6014f779575adfd29373c228edd4 | hotkey 5EZx1DRvpMGK…
2026-05-24 09:12:17     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:12:17    Downloading Lin2es/evolai-mb2-04v@9c0198682f16cc8595fec849aa37227f7160e92c…
2026-05-24 09:12:17     Fetched 20 texts (20 indices)
2026-05-24 09:12:19     Loaded (local prefetch)
2026-05-24 09:12:19     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 09:12:21   [6/15] UID 41 | Radiant28/evolai-mamba2-0.47b-v3 @
2026-05-24 09:12:21 97f692fb0b295aa29075d3f9d592bfb4e7625b16 | hotkey 5CP5QrWuFe93…
2026-05-24 09:12:21     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:12:21     Fetched 20 texts (20 indices)
2026-05-24 09:12:21    Ready: Lin2es/evolai-mb2-04v@9c0198682f16cc8595fec849aa37227f7160e92c
2026-05-24 09:12:21    Downloading
2026-05-24 09:12:21 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518…
2026-05-24 09:12:22     Loaded (local prefetch)
2026-05-24 09:12:23     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 09:12:25   [7/15] UID 89 | Lin2es/evolai-mb2-04v @
2026-05-24 09:12:25 9c0198682f16cc8595fec849aa37227f7160e92c | hotkey 5DkZf6V3X8Za…
2026-05-24 09:12:25     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:12:25     Fetched 20 texts (20 indices)
2026-05-24 09:12:25    Ready:
2026-05-24 09:12:25 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518
2026-05-24 09:12:25    Downloading Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd…
2026-05-24 09:12:26     Loaded (local prefetch)
2026-05-24 09:12:26     ⚠ Vocab incompatible (model=151665 < ref=248077) — skipping
2026-05-24 09:12:27    Ready: Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd
2026-05-24 09:12:28   [8/15] UID 30 | mihai-777/evolai-mamba2-0p47b-v3 @
2026-05-24 09:12:28 c2a96b92acf632d51a2c21da4482f77f98256518 | hotkey 5GGsbuVKDrTA…
2026-05-24 09:12:28     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:12:28     Fetched 20 texts (20 indices)
2026-05-24 09:12:28    Downloading
2026-05-24 09:12:28 mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7…
2026-05-24 09:12:29     Loaded (local prefetch)
2026-05-24 09:12:30     Model 0.48B → batch=512, seq=16384
2026-05-24 09:12:32    Ready: mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7
2026-05-24 09:12:34     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 09:12:34     Loss 4.8587 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:12:34 0.1069 | KL 4.8587 | NextKL 4.7301 | SideQ 0% | Score 0.0000 (4.1s)
2026-05-24 09:12:34     Gate FAIL | Improve same SHA cur=4.8587 req<=4.7616 prev=4.8587 | Consist ok
2026-05-24 09:12:34 ema_cur=4.7955 ema_next=4.7948 ratio=1.000 max<=1.20
2026-05-24 09:12:35   Evicted cached model:
2026-05-24 09:12:35 Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59
2026-05-24 09:12:36   [9/15] UID 91 | Lin2es/evolai-mb2-03v @
2026-05-24 09:12:36 3047597c4e4b4430450ddcd633240b88d781fdbd | hotkey 5EcdUqvUBCSp…
2026-05-24 09:12:36     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:12:36    Downloading Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0…
2026-05-24 09:12:36     Fetched 20 texts (20 indices)
2026-05-24 09:12:37     Loaded (local prefetch)
2026-05-24 09:12:38     Model 0.48B → batch=512, seq=16384
2026-05-24 09:12:39    Ready: Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0
2026-05-24 09:12:42     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 09:12:42     Loss 4.7157 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:12:42 0.0000 | KL 4.7157 | NextKL 4.6332 | SideQ 0% | Score 0.0000 (4.1s)
2026-05-24 09:12:42     Gate FAIL | Improve same SHA cur=4.7157 req<=4.6214 prev=4.7157 | Consist ok
2026-05-24 09:12:42 ema_cur=4.6678 ema_next=4.6675 ratio=1.000 max<=1.20
2026-05-24 09:12:44   Evicted cached model:
2026-05-24 09:12:44 clear-blue-sky/evolai-reborn-tfm-001@5233a721363395c7abfdcfad299f43520b003100
2026-05-24 09:12:44   [10/15] UID 31 | mihai-777/evolai-mamba2-0p47b @
2026-05-24 09:12:44 7b6564c9a46f602702c260185aa43867f321dee7 | hotkey 5CJuKKq16FkR…
2026-05-24 09:12:44     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:12:44    Downloading
2026-05-24 09:12:44 andrebarrosilva1123/evolai-mamba2-c@dc37c985d66c77e3d10bf9eaf16e6dc952c62e17…
2026-05-24 09:12:44     Fetched 20 texts (20 indices)
2026-05-24 09:12:45     Loaded (local prefetch)
2026-05-24 09:12:46     Model 0.48B → batch=512, seq=16384
2026-05-24 09:12:47    Ready:
2026-05-24 09:12:47 andrebarrosilva1123/evolai-mamba2-c@dc37c985d66c77e3d10bf9eaf16e6dc952c62e17
2026-05-24 09:12:50     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 09:12:50     Loss 4.8183 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:12:50 0.0000 | KL 4.8183 | NextKL 4.7761 | SideQ 0% | Score 0.0000 (4.1s)
2026-05-24 09:12:50     Gate FAIL | Improve same SHA cur=4.8183 req<=4.7219 prev=4.8183 | Consist ok
2026-05-24 09:12:50 ema_cur=4.7753 ema_next=4.7700 ratio=0.999 max<=1.20
2026-05-24 09:12:52   Evicted cached model:
2026-05-24 09:12:52 clear-blue-sky/evolai-reborn-tfm-005@455b69e426e6ca0721b3f69943223fe21173d569
2026-05-24 09:12:52   [11/15] UID 11 | Lin2es/evolai-mb2-01v @
2026-05-24 09:12:52 a7f32e5ce7f8d307c98560e5025525f3703310c0 | hotkey 5HYuS4jrJJ56…
2026-05-24 09:12:52     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:12:52     Fetched 20 texts (20 indices)
2026-05-24 09:12:52    Downloading
2026-05-24 09:12:52 evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a…
2026-05-24 09:12:54     Loaded (local prefetch)
2026-05-24 09:12:54     Model 0.48B → batch=512, seq=16384
2026-05-24 09:12:55    Ready: evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a
2026-05-24 09:12:58     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 09:12:58     Loss 4.6361 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:12:58 0.1604 | KL 4.6361 | NextKL 4.7182 | SideQ 0% | Score 0.0000 (4.0s)
2026-05-24 09:12:58     Gate FAIL | Improve same SHA cur=4.6361 req<=4.5434 prev=4.6361 | Consist ok
2026-05-24 09:12:58 ema_cur=4.6499 ema_next=4.6653 ratio=1.003 max<=1.20
2026-05-24 09:13:00   Evicted cached model:
2026-05-24 09:13:00 Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4
2026-05-24 09:13:00   [12/15] UID 58 | andrebarrosilva1123/evolai-mamba2-c @
2026-05-24 09:13:00 dc37c985d66c77e3d10bf9eaf16e6dc952c62e17 | hotkey 5EgtSzXJbjpV…
2026-05-24 09:13:00     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:13:00    Downloading
2026-05-24 09:13:00 Radiant28/evolai-mamba2-0.47b-v2@475bf7bf65af1192ed824d58816c1d83f3475983…
2026-05-24 09:13:00     Fetched 20 texts (20 indices)
2026-05-24 09:13:01     Loaded (local prefetch)
2026-05-24 09:13:02     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 09:13:03   [13/15] UID 96 | evolai/evolai_mamba_naive_kl @
2026-05-24 09:13:03 b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a | hotkey 5HQuJVXBXGrW…
2026-05-24 09:13:03     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:13:03     Fetched 20 texts (20 indices)
2026-05-24 09:13:03    Ready:
2026-05-24 09:13:03 Radiant28/evolai-mamba2-0.47b-v2@475bf7bf65af1192ed824d58816c1d83f3475983
2026-05-24 09:13:03    Downloading
2026-05-24 09:13:03 batster4/evolai-mamba2-v1@142f14d218be618e3161d86926085b3a9cefed55…
2026-05-24 09:13:05     Loaded (local prefetch)
2026-05-24 09:13:05     Model 0.46B → batch=512, seq=16384
2026-05-24 09:13:07    Ready: batster4/evolai-mamba2-v1@142f14d218be618e3161d86926085b3a9cefed55
2026-05-24 09:13:09     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 09:13:09     Loss 3.5533 | Size ×0.50 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:13:09 0.0000 | KL 3.5533 | NextKL 3.1070 | SideQ 0% | Score 0.0000 (4.0s)
2026-05-24 09:13:09     Gate FAIL | Improve same SHA cur=3.5533 req<=3.4823 prev=3.5533 | Consist ok
2026-05-24 09:13:09 ema_cur=4.0255 ema_next=3.4656 ratio=0.861 max<=1.20
2026-05-24 09:13:10   Evicted cached model:
2026-05-24 09:13:10 clear-blue-sky/evolai-reborn-tfm-008@819b51083eb5f5e01d1a1e50c836daf868e0f1e7
2026-05-24 09:13:11   [14/15] UID 39 | Radiant28/evolai-mamba2-0.47b-v2 @
2026-05-24 09:13:11 475bf7bf65af1192ed824d58816c1d83f3475983 | hotkey 5FvTt3gVVhFT…
2026-05-24 09:13:11     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:13:11     Fetched 20 texts (20 indices)
2026-05-24 09:13:12     Loaded (local prefetch)
2026-05-24 09:13:13     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 09:13:14   [15/15] UID 60 | batster4/evolai-mamba2-v1 @
2026-05-24 09:13:14 142f14d218be618e3161d86926085b3a9cefed55 | hotkey 5Dc8EpAixcqc…
2026-05-24 09:13:14     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:13:14     Fetched 20 texts (20 indices)
2026-05-24 09:13:16     Loaded (local prefetch)
2026-05-24 09:13:16     ⚠ Invalid model size (0.82B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 09:13:18   Cached next refs for mamba2: 15 miner(s)
2026-05-24 09:13:18 
2026-05-24 09:13:18   ✓ MAMBA2: 7 evaluated, 14 skipped — epoch_22924_mamba2_20260524_084503.json
2026-05-24 09:13:18   ✓ Telemetry sent (7 records)
2026-05-24 09:13:18 Current Leaderboard:
2026-05-24 09:13:31 
2026-05-24 09:13:31    alpha=0.005455 TAO/α  budget=0.049683
2026-05-24 09:13:33 TRANSFORMER
2026-05-24 09:13:33 ┏━━━━━━┳━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━━━┳━━━━━━━┓
2026-05-24 09:13:33 ┃      ┃     ┃        ┃     Latest ┃           ┃       ┃     ┃         ┃       ┃
2026-05-24 09:13:33 ┃ Rank ┃ UID ┃  Score ┃       Loss ┃ ThinkGain ┃  Flow ┃ SQ% ┃      KL ┃ Evals ┃
2026-05-24 09:13:33 ┡━━━━━━╇━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━━━╇━━━━━━━┩
2026-05-24 09:13:33 │    1 │   8 │ 0.0310 │     3.8917 │  0 FAIL   │ 0.000 │  0% │  1.7940 │   308 │
2026-05-24 09:13:33 │    2 │  82 │ 0.0000 │     3.8200 │  0 FAIL   │ 0.217 │  0% │  1.8514 │   343 │
2026-05-24 09:13:33 │    3 │  66 │ 0.0000 │     3.7772 │  0 FAIL   │ 0.000 │  0% │  1.9541 │   343 │
2026-05-24 09:13:33 │    4 │  87 │ 0.0000 │     4.0577 │  0 FAIL   │ 0.133 │  0% │  2.2495 │   147 │
2026-05-24 09:13:33 │    5 │  86 │ 0.0000 │     4.1094 │  0 FAIL   │ 0.139 │  0% │  2.3171 │   148 │
2026-05-24 09:13:33 │    6 │  73 │ 0.0000 │     3.6379 │  0 FAIL   │ 0.000 │  0% │  1.8415 │   128 │
2026-05-24 09:13:33 │    7 │  93 │ 0.0000 │     3.9991 │  0 FAIL   │ 0.000 │  0% │  2.1836 │   128 │
2026-05-24 09:13:33 │    8 │  97 │ 0.0000 │     3.7542 │  0 FAIL   │ 0.000 │  0% │  1.9200 │   258 │
2026-05-24 09:13:33 │    9 │  67 │ 0.0000 │     3.8033 │  0 FAIL   │ 0.383 │  0% │  1.9292 │   345 │
2026-05-24 09:13:33 │   10 │  70 │ 0.0000 │     4.0522 │  0 FAIL   │ 0.000 │  0% │  1.9079 │   343 │
2026-05-24 09:13:33 │   11 │  83 │ 0.0000 │     3.8881 │  0 FAIL   │ 0.000 │  0% │  1.8725 │   345 │
2026-05-24 09:13:33 │   12 │  85 │ 0.0000 │     3.9816 │  0 FAIL   │ 0.000 │  0% │  2.0327 │   332 │
2026-05-24 09:13:33 │   13 │  99 │ 0.0000 │     4.0723 │  0 FAIL   │ 0.000 │  0% │  1.9656 │   126 │
2026-05-24 09:13:33 │   14 │  72 │ 0.0000 │     3.6976 │  0 FAIL   │ 0.186 │  0% │  1.6246 │   127 │
2026-05-24 09:13:33 │   15 │  62 │ 0.0000 │     3.8803 │  0 FAIL   │ 0.000 │  0% │  1.8842 │   345 │
2026-05-24 09:13:33 │   16 │  94 │ 0.0000 │     4.0320 │  0 FAIL   │ 0.000 │  0% │  1.9489 │   258 │
2026-05-24 09:13:33 │   17 │  98 │ 0.0000 │     4.0897 │  0 FAIL   │ 0.029 │  0% │  2.0044 │   257 │
2026-05-24 09:13:33 │   18 │  69 │ 0.0000 │     3.4968 │  0 FAIL   │ 0.385 │  0% │  1.6931 │   128 │
2026-05-24 09:13:33 │   19 │  48 │ 0.0000 │     3.8975 │  0 FAIL   │ 0.165 │  0% │  1.9501 │   132 │
2026-05-24 09:13:33 │   20 │   9 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 09:13:33 │   21 │  25 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 09:13:33 │   22 │  33 │ 0.0000 │     3.2509 │  0 FAIL   │ 0.000 │  0% │  2.5351 │   345 │
2026-05-24 09:13:33 │   23 │  35 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:13:33 │   24 │  36 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 09:13:33 │   25 │  37 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:13:33 │   26 │  38 │ 0.0000 │     3.3598 │  0 FAIL   │ 0.198 │  0% │  2.4190 │   344 │
2026-05-24 09:13:33 │   27 │  40 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:13:33 │   28 │  42 │ 0.0000 │     3.1897 │  0 FAIL   │ 0.167 │  0% │  2.4519 │   345 │
2026-05-24 09:13:33 │   29 │  43 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:13:33 │   30 │  44 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 09:13:33 │   31 │  45 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:13:33 │   32 │  49 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 09:13:33 │   33 │  50 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 09:13:33 │   34 │  51 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   317 │
2026-05-24 09:13:33 │   35 │  52 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   318 │
2026-05-24 09:13:33 │   36 │  53 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:13:33 │   37 │  54 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   316 │
2026-05-24 09:13:33 │   38 │  55 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 09:13:33 │   39 │  59 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:13:33 │   40 │  61 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:13:33 │   41 │  65 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:13:33 │   42 │  75 │ 0.0000 │     2.8941 │  0 FAIL   │ 0.292 │  0% │  2.2630 │   346 │
2026-05-24 09:13:33 │   43 │  76 │ 0.0000 │     2.7042 │  0 FAIL   │ 0.038 │  0% │  1.9994 │   344 │
2026-05-24 09:13:33 │   44 │  77 │ 0.0000 │     2.1734 │  0 FAIL   │ 0.000 │  0% │  2.3550 │   247 │
2026-05-24 09:13:33 │   45 │  78 │ 0.0000 │     2.6394 │  0 FAIL   │ 0.000 │  0% │  2.8060 │   247 │
2026-05-24 09:13:33 │   46 │  79 │ 0.0000 │     2.3688 │  0 FAIL   │ 0.002 │  0% │  2.6815 │   247 │
2026-05-24 09:13:33 │   47 │  80 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 09:13:33 │   48 │  84 │ 0.0000 │     3.9665 │  0 FAIL   │ 0.000 │  0% │  1.8725 │   329 │
2026-05-24 09:13:33 │   49 │  88 │ 0.0000 │     3.9147 │  0 FAIL   │ 0.290 │  0% │  1.9992 │   146 │
2026-05-24 09:13:33 │   50 │  92 │ 0.0000 │     2.1641 │  0 FAIL   │ 0.000 │  0% │  2.1930 │   248 │
2026-05-24 09:13:33 │   51 │  95 │ 0.0000 │     3.1120 │  0 FAIL   │ 0.084 │  0% │  2.6833 │   257 │
2026-05-24 09:13:33 │   52 │ 100 │ 0.0000 │     4.0175 │  0 FAIL   │ 0.000 │  0% │  3.8966 │   256 │
2026-05-24 09:13:33 │   53 │ 101 │ 0.0000 │     3.6719 │  0 FAIL   │ 0.327 │  0% │  1.7446 │    78 │
2026-05-24 09:13:33 └──────┴─────┴────────┴────────────┴───────────┴───────┴─────┴─────────┴───────┘
2026-05-24 09:13:33 
2026-05-24 09:13:33 MAMBA2
2026-05-24 09:13:33 ┏━━━━━━┳━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━━━┳━━━━━━━┓
2026-05-24 09:13:33 ┃      ┃     ┃        ┃     Latest ┃           ┃       ┃     ┃         ┃       ┃
2026-05-24 09:13:33 ┃ Rank ┃ UID ┃  Score ┃       Loss ┃ ThinkGain ┃  Flow ┃ SQ% ┃      KL ┃ Evals ┃
2026-05-24 09:13:33 ┡━━━━━━╇━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━━━╇━━━━━━━┩
2026-05-24 09:13:33 │    1 │  11 │ 0.0000 │     4.6361 │  0 FAIL   │ 0.160 │  0% │  4.6361 │   247 │
2026-05-24 09:13:33 │    2 │  30 │ 0.0000 │     4.8587 │  0 FAIL   │ 0.107 │  0% │  4.8587 │   342 │
2026-05-24 09:13:33 │    3 │  31 │ 0.0000 │     4.8183 │  0 FAIL   │ 0.000 │  0% │  4.8183 │   342 │
2026-05-24 09:13:33 │    4 │  32 │ 0.0000 │     4.7938 │  0 FAIL   │ 0.000 │  0% │  4.7938 │   342 │
2026-05-24 09:13:33 │    5 │  34 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   342 │
2026-05-24 09:13:33 │    6 │  39 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   343 │
2026-05-24 09:13:33 │    7 │  41 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   342 │
2026-05-24 09:13:33 │    8 │  56 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   342 │
2026-05-24 09:13:33 │    9 │  57 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   342 │
2026-05-24 09:13:33 │   10 │  58 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   342 │
2026-05-24 09:13:33 │   11 │  60 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   342 │
2026-05-24 09:13:33 │   12 │  63 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   271 │
2026-05-24 09:13:33 │   13 │  64 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 09:13:33 │   14 │  68 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 09:13:33 │   15 │  71 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   271 │
2026-05-24 09:13:33 │   16 │  74 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 09:13:33 │   17 │  81 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   273 │
2026-05-24 09:13:33 │   18 │  89 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   247 │
2026-05-24 09:13:33 │   19 │  90 │ 0.0000 │     4.7356 │  0 FAIL   │ 0.000 │  0% │  4.7356 │   257 │
2026-05-24 09:13:33 │   20 │  91 │ 0.0000 │     4.7157 │  0 FAIL   │ 0.000 │  0% │  4.7157 │   257 │
2026-05-24 09:13:33 │   21 │  96 │ 0.0000 │     3.5533 │  0 FAIL   │ 0.000 │  0% │  3.5533 │   257 │
2026-05-24 09:13:33 └──────┴─────┴────────┴────────────┴───────────┴───────┴─────┴─────────┴───────┘
2026-05-24 09:13:33 
2026-05-24 09:13:33 Round complete in epoch 22924 (1710s elapsed). Starting next round immediately…
2026-05-24 09:13:33 
2026-05-24 09:13:33 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2026-05-24 09:13:33 
2026-05-24 09:13:33 ━━━ Epoch #22924 (Loop #3) ━━━ block=8252978, ~4m remaining
2026-05-24 09:13:42 
2026-05-24 09:13:42   ⚠ UID 86: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:13:42 (Request ID:
2026-05-24 09:13:42 Root=1-6a12c146-499301bf52652e2c26d2bd02;e30c5873-f2c3-4732-a1f5-fe117d0979b2)
2026-05-24 09:13:42 
2026-05-24 09:13:42 Repository Not Found for url:
2026-05-24 09:13:42 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-012/revision/main.
2026-05-24 09:13:42 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:13:42 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:13:42 authenticated and your token has the required permissions.
2026-05-24 09:13:42 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:13:42 Invalid username or password.
2026-05-24 09:13:42   ⚠ UID 87: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:13:42 (Request ID:
2026-05-24 09:13:42 Root=1-6a12c146-0aee4b5c4c6dca096af96276;4b55d87c-d95a-49b3-af7c-0eecb3e08f77)
2026-05-24 09:13:42 
2026-05-24 09:13:42 Repository Not Found for url:
2026-05-24 09:13:42 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-013/revision/main.
2026-05-24 09:13:42 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:13:42 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:13:42 authenticated and your token has the required permissions.
2026-05-24 09:13:42 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:13:42 Invalid username or password.
2026-05-24 09:13:43   ⚠ UID 88: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:13:43 (Request ID:
2026-05-24 09:13:43 Root=1-6a12c147-752b643c354fa4dd39093f4b;b9ff3cf8-fbdf-4e36-b213-3fe5c7e4c22a)
2026-05-24 09:13:43 
2026-05-24 09:13:43 Repository Not Found for url:
2026-05-24 09:13:43 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-014/revision/main.
2026-05-24 09:13:43 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:13:43 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:13:43 authenticated and your token has the required permissions.
2026-05-24 09:13:43 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:13:43 Invalid username or password.
2026-05-24 09:13:43   Locked transformer revisions (50 miner(s), 3 skipped)
2026-05-24 09:13:45    emission scale=1.000 (active miners)
2026-05-24 09:13:46    emission scale=1.000 (active miners)
2026-05-24 09:13:46    all quality scores zero after gates — emission share redistributed to
2026-05-24 09:13:46 productive tracks
2026-05-24 09:13:47   ✓  set at 09:13:47 UTC
2026-05-24 09:13:52   ⚠ UID 63: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:13:52 (Request ID:
2026-05-24 09:13:52 Root=1-6a12c150-1b3b784757c023674f9472c6;88f95ee5-b8be-47d9-a665-4701bc14ae43)
2026-05-24 09:13:52 
2026-05-24 09:13:52 Repository Not Found for url:
2026-05-24 09:13:52 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-009/revision/main.
2026-05-24 09:13:52 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:13:52 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:13:52 authenticated and your token has the required permissions.
2026-05-24 09:13:52 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:13:52 Invalid username or password.
2026-05-24 09:13:52   ⚠ UID 64: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:13:52 (Request ID:
2026-05-24 09:13:52 Root=1-6a12c150-32aafe104c28694875c1930b;54a30620-d236-4901-ab93-65d1eb63cf27)
2026-05-24 09:13:52 
2026-05-24 09:13:52 Repository Not Found for url:
2026-05-24 09:13:52 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-002/revision/main.
2026-05-24 09:13:52 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:13:52 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:13:52 authenticated and your token has the required permissions.
2026-05-24 09:13:52 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:13:52 Invalid username or password.
2026-05-24 09:13:52   ⚠ UID 68: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:13:52 (Request ID:
2026-05-24 09:13:52 Root=1-6a12c150-0060af552a67314212854c74;0125fc38-8c63-4468-ac82-d6a8a83732fc)
2026-05-24 09:13:52 
2026-05-24 09:13:52 Repository Not Found for url:
2026-05-24 09:13:52 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-008/revision/main.
2026-05-24 09:13:52 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:13:52 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:13:52 authenticated and your token has the required permissions.
2026-05-24 09:13:52 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:13:52 Invalid username or password.
2026-05-24 09:13:52   ⚠ UID 71: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:13:52 (Request ID:
2026-05-24 09:13:52 Root=1-6a12c150-5d4b93b57ee571f75f490756;91670a5f-fd3e-4a46-962b-d9ba285be366)
2026-05-24 09:13:52 
2026-05-24 09:13:52 Repository Not Found for url:
2026-05-24 09:13:52 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-001/revision/main.
2026-05-24 09:13:52 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:13:52 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:13:52 authenticated and your token has the required permissions.
2026-05-24 09:13:52 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:13:52 Invalid username or password.
2026-05-24 09:13:52   ⚠ UID 74: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:13:52 (Request ID:
2026-05-24 09:13:52 Root=1-6a12c150-4852384b455dc87358a61229;31703c99-b5f7-432e-b1a0-44f45788e3c1)
2026-05-24 09:13:52 
2026-05-24 09:13:52 Repository Not Found for url:
2026-05-24 09:13:52 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-007/revision/main.
2026-05-24 09:13:52 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:13:52 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:13:52 authenticated and your token has the required permissions.
2026-05-24 09:13:52 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:13:52 Invalid username or password.
2026-05-24 09:13:52   ⚠ UID 81: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:13:52 (Request ID:
2026-05-24 09:13:52 Root=1-6a12c150-5426b1ef4ca3e0f740c2af8a;1f2c3ebc-ab02-48a9-8ea3-7ca667e51d68)
2026-05-24 09:13:52 
2026-05-24 09:13:52 Repository Not Found for url:
2026-05-24 09:13:52 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-010/revision/main.
2026-05-24 09:13:52 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:13:52 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:13:52 authenticated and your token has the required permissions.
2026-05-24 09:13:52 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:13:52 Invalid username or password.
2026-05-24 09:13:52   Locked mamba2 revisions (15 miner(s), 6 skipped)
2026-05-24 09:13:52   Waiting 9.8s before seed commit (weight-set nonce cooldown)...
2026-05-24 09:14:39   Committed round seed epoch=22924 seed=b5396236...
2026-05-24 09:14:39 Evaluating TRANSFORMER track…
2026-05-24 09:14:39 
2026-05-24 09:14:39   Found 50 locked transformer miners
2026-05-24 09:14:39    Downloading
2026-05-24 09:14:39 andrebarrosilva1123/evolai-b@3414c0abb8793ed4af56fd5e6e536b8b0f5ac520…
2026-05-24 09:14:39 Pre-building current/next challenges for 50 miners…
2026-05-24 09:14:39 Fetching 7 files: 100%|██████████| 7/7 [00:06<00:00,  1.10it/s]
2026-05-24 09:14:46    Ready: andrebarrosilva1123/evolai-b@3414c0abb8793ed4af56fd5e6e536b8b0f5ac520
2026-05-24 09:14:46    Downloading
2026-05-24 09:14:46 logosnodos/evolai-qwen-1.5b@7e121e8efe6c6b93d622e9a53972d221e763d10b…
2026-05-24 09:14:46 Fetching 17 files: 100%|██████████| 17/17 [00:43<00:00,  2.53s/it]
2026-05-24 09:15:29    Ready: logosnodos/evolai-qwen-1.5b@7e121e8efe6c6b93d622e9a53972d221e763d10b
2026-05-24 09:15:49 ✓ Ref data ready: submitted=50, cached=50
2026-05-24 09:15:49   [1/50] UID 50 | andrebarrosilva1123/evolai-b @
2026-05-24 09:15:49 3414c0abb8793ed4af56fd5e6e536b8b0f5ac520 | hotkey 5FXELcBK4WiD…
2026-05-24 09:15:49     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:15:49     Fetched 20 texts (20 indices)
2026-05-24 09:15:49    Downloading
2026-05-24 09:15:49 andrebarrosilva1123/evolai-0.4b@fa913c93aa7a7449066ce870427387bd3fc7e841…
2026-05-24 09:15:51     Loaded (local prefetch)
2026-05-24 09:15:52     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:15:54   [2/50] UID 61 | logosnodos/evolai-qwen-1.5b @
2026-05-24 09:15:54 7e121e8efe6c6b93d622e9a53972d221e763d10b | hotkey 5FNTU6ZYgKup…
2026-05-24 09:15:54     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:15:54     Fetched 20 texts (20 indices)
2026-05-24 09:15:55    Ready:
2026-05-24 09:15:55 andrebarrosilva1123/evolai-0.4b@fa913c93aa7a7449066ce870427387bd3fc7e841
2026-05-24 09:15:55    Downloading
2026-05-24 09:15:55 mrthor102/evolai-tfm-super-003@75d4671ce2bf769be9ded4bd4205abef791212d1…
2026-05-24 09:15:57     Loaded (local prefetch)
2026-05-24 09:16:00    Ready:
2026-05-24 09:16:00 mrthor102/evolai-tfm-super-003@75d4671ce2bf769be9ded4bd4205abef791212d1
2026-05-24 09:16:02     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:16:04   [3/50] UID 49 | andrebarrosilva1123/evolai-0.4b @
2026-05-24 09:16:04 fa913c93aa7a7449066ce870427387bd3fc7e841 | hotkey 5DULz3AJEisH…
2026-05-24 09:16:04     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:16:04     Fetched 20 texts (20 indices)
2026-05-24 09:16:04    Downloading
2026-05-24 09:16:04 clear-blue-sky/evolai-reborn-tfm-011@3c6fb9eda1f125661a5c6e9f4243ace37e38e4b5…
2026-05-24 09:16:06     Loaded (local prefetch)
2026-05-24 09:16:07     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:16:09   [4/50] UID 98 | mrthor102/evolai-tfm-super-003 @
2026-05-24 09:16:09 75d4671ce2bf769be9ded4bd4205abef791212d1 | hotkey 5Hgy59m2Hzm1…
2026-05-24 09:16:09     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:16:09     Fetched 20 texts (20 indices)
2026-05-24 09:16:09    Ready:
2026-05-24 09:16:09 clear-blue-sky/evolai-reborn-tfm-011@3c6fb9eda1f125661a5c6e9f4243ace37e38e4b5
2026-05-24 09:16:09    Downloading
2026-05-24 09:16:09 Radiant28/evolai-transformer-0.4b-b2@808b61992e043ca99ff5b412a6cf61bfbb3fd793…
2026-05-24 09:16:12     Loaded (local prefetch)
2026-05-24 09:16:12     Model 0.46B → batch=512, seq=16384
2026-05-24 09:16:15    Ready:
2026-05-24 09:16:15 Radiant28/evolai-transformer-0.4b-b2@808b61992e043ca99ff5b412a6cf61bfbb3fd793
2026-05-24 09:17:12     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:56
2026-05-24 09:17:12     Loss 4.0643 | Size ×0.50 | Think 4.0643 | ThinkGain 0 (+0.4604) | Flow
2026-05-24 09:17:12 0.0739 | KL 1.8700 | NextKL 2.2070 | SideQ 0% | Score 0.0000 (59.4s)
2026-05-24 09:17:12     Gate FAIL | Improve same SHA cur=1.8700 req<=1.8326 prev=1.8700 | Consist ok
2026-05-24 09:17:12 ema_cur=1.9112 ema_next=1.9388 ratio=1.014 max<=1.20
2026-05-24 09:17:13   Evicted cached model:
2026-05-24 09:17:13 Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8
2026-05-24 09:17:14   [5/50] UID 73 | clear-blue-sky/evolai-reborn-tfm-011 @
2026-05-24 09:17:14 3c6fb9eda1f125661a5c6e9f4243ace37e38e4b5 | hotkey 5CSAM6rnGRPk…
2026-05-24 09:17:14     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:17:14     Fetched 20 texts (20 indices)
2026-05-24 09:17:14    Downloading
2026-05-24 09:17:14 mrthor102/evolai-tfm-super-002@db9483fdd7fb46c99ba8731900ec009330f4e77e…
2026-05-24 09:17:15     Loaded (local prefetch)
2026-05-24 09:17:16     Model 0.46B → batch=512, seq=16384
2026-05-24 09:17:18    Ready:
2026-05-24 09:17:18 mrthor102/evolai-tfm-super-002@db9483fdd7fb46c99ba8731900ec009330f4e77e
2026-05-24 09:18:17     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:55
2026-05-24 09:18:18     Loss 3.8881 | Size ×0.50 | Think 3.8881 | ThinkGain 0 (+0.4628) | Flow
2026-05-24 09:18:18 0.0000 | KL 1.7976 | NextKL 1.8382 | SideQ 0% | Score 0.0000 (61.3s)
2026-05-24 09:18:18     Gate FAIL | Improve same SHA cur=1.7976 req<=1.7616 prev=1.7976 | Consist ok
2026-05-24 09:18:18 ema_cur=2.4428 ema_next=1.8533 ratio=0.759 max<=1.20
2026-05-24 09:18:20   Evicted cached model:
2026-05-24 09:18:20 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c
2026-05-24 09:18:21   [6/50] UID 37 | Radiant28/evolai-transformer-0.4b-b2 @
2026-05-24 09:18:21 808b61992e043ca99ff5b412a6cf61bfbb3fd793 | hotkey 5HjbzF3e9waA…
2026-05-24 09:18:21     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:18:21     Fetched 20 texts (20 indices)
2026-05-24 09:18:21    Downloading
2026-05-24 09:18:21 mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c…
2026-05-24 09:18:23     Loaded (local prefetch)
2026-05-24 09:18:24     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:18:25    Ready: mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c
2026-05-24 09:18:26   [7/50] UID 97 | mrthor102/evolai-tfm-super-002 @
2026-05-24 09:18:26 db9483fdd7fb46c99ba8731900ec009330f4e77e | hotkey 5EcJYRJBVF5K…
2026-05-24 09:18:26     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:18:26     Fetched 20 texts (20 indices)
2026-05-24 09:18:26    Downloading
2026-05-24 09:18:26 mrthor102/evolai-tfm-super-001@c2dac74023c984bf5261f93f33f748659f16f224…
2026-05-24 09:18:28     Loaded (local prefetch)
2026-05-24 09:18:28     Model 0.46B → batch=512, seq=16384
2026-05-24 09:18:30    Ready:
2026-05-24 09:18:30 mrthor102/evolai-tfm-super-001@c2dac74023c984bf5261f93f33f748659f16f224
2026-05-24 09:19:30     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:56
2026-05-24 09:19:30     Loss 3.7057 | Size ×0.50 | Think 3.7057 | ThinkGain 0 (+0.4624) | Flow
2026-05-24 09:19:30 0.0000 | KL 2.0417 | NextKL 1.9717 | SideQ 0% | Score 0.0000 (61.5s)
2026-05-24 09:19:30     Gate FAIL | Improve same SHA cur=2.0417 req<=2.0008 prev=2.0417 | Consist ok
2026-05-24 09:19:30 ema_cur=1.9419 ema_next=1.9426 ratio=1.000 max<=1.20
2026-05-24 09:19:31   Evicted cached model:
2026-05-24 09:19:31 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518
2026-05-24 09:19:32   [8/50] UID 33 | mihai-777/evolai-tfm-1p5b @
2026-05-24 09:19:32 594894f806fb4c014675d89aad14f1c68976d52c | hotkey 5F22JM4of6TR…
2026-05-24 09:19:32     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:19:32     Fetched 20 texts (20 indices)
2026-05-24 09:19:32    Downloading snx999/evolai_qw_4b@69eff663b4e9a2b5bf76dde6cdecc5dce29759d3…
2026-05-24 09:19:34     Loaded (local prefetch)
2026-05-24 09:19:34     Model 0.46B → batch=512, seq=16384
2026-05-24 09:19:53    Ready: snx999/evolai_qw_4b@69eff663b4e9a2b5bf76dde6cdecc5dce29759d3
2026-05-24 09:20:38     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:59
2026-05-24 09:20:39     Loss 2.4238 | Size ×0.50 | Think 2.4238 | ThinkGain 0 (+0.4524) | Flow
2026-05-24 09:20:39 0.0628 | KL 2.2523 | NextKL 2.2735 | SideQ 0% | Score 0.0000 (64.3s)
2026-05-24 09:20:39     Gate FAIL | Improve same SHA cur=2.2523 req<=2.2073 prev=2.2523 | Consist ok
2026-05-24 09:20:39 ema_cur=2.3984 ema_next=2.4024 ratio=1.002 max<=1.20
2026-05-24 09:20:41   Evicted cached model:
2026-05-24 09:20:41 Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd
2026-05-24 09:20:41   [9/50] UID 94 | mrthor102/evolai-tfm-super-001 @
2026-05-24 09:20:41 c2dac74023c984bf5261f93f33f748659f16f224 | hotkey 5CPXihPMoGQ2…
2026-05-24 09:20:41     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:20:41     Fetched 20 texts (20 indices)
2026-05-24 09:20:41    Downloading
2026-05-24 09:20:41 Radiant28/evolai-transformer-0.4b-b0@7a08a8009fa8b8f82d1ad0febc442a89020082d1…
2026-05-24 09:20:43     Loaded (local prefetch)
2026-05-24 09:20:43     Model 0.46B → batch=512, seq=16384
2026-05-24 09:20:49    Ready:
2026-05-24 09:20:49 Radiant28/evolai-transformer-0.4b-b0@7a08a8009fa8b8f82d1ad0febc442a89020082d1
2026-05-24 09:21:34     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:47
2026-05-24 09:21:34     Loss 3.6372 | Size ×0.50 | Think 3.6372 | ThinkGain 0 (+0.4574) | Flow
2026-05-24 09:21:34 0.1178 | KL 1.6471 | NextKL 2.0071 | SideQ 0% | Score 0.0000 (50.4s)
2026-05-24 09:21:34     Gate FAIL | Improve same SHA cur=1.6471 req<=1.6142 prev=1.6471 | Consist ok
2026-05-24 09:21:34 ema_cur=1.9008 ema_next=1.9230 ratio=1.012 max<=1.20
2026-05-24 09:21:35   Evicted cached model:
2026-05-24 09:21:35 mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7
2026-05-24 09:21:36   [10/50] UID 25 | snx999/evolai_qw_4b @
2026-05-24 09:21:36 69eff663b4e9a2b5bf76dde6cdecc5dce29759d3 | hotkey 5HBJoNWv4nAi…
2026-05-24 09:21:36     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:21:36     Fetched 20 texts (20 indices)
2026-05-24 09:21:36    Downloading
2026-05-24 09:21:36 clear-blue-sky/evolai-reborn-tfm-002@9d512cab2a9007b7d58a6ec4988e6ac869910be5…
2026-05-24 09:21:39     Loaded (local prefetch)
2026-05-24 09:21:40    Ready:
2026-05-24 09:21:40 clear-blue-sky/evolai-reborn-tfm-002@9d512cab2a9007b7d58a6ec4988e6ac869910be5
2026-05-24 09:21:40     ⚠ Invalid model size (4.21B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 09:21:42   [11/50] UID 45 | Radiant28/evolai-transformer-0.4b-b0 @
2026-05-24 09:21:42 7a08a8009fa8b8f82d1ad0febc442a89020082d1 | hotkey 5F1B3j7EyjuE…
2026-05-24 09:21:42     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:21:42     Fetched 20 texts (20 indices)
2026-05-24 09:21:42    Downloading
2026-05-24 09:21:42 clear-blue-sky/evolai-reborn-tfm-010@a925485d558b5b141050fd8bc943880e4a97b289…
2026-05-24 09:21:44     Loaded (local prefetch)
2026-05-24 09:21:44     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:21:46   [12/50] UID 67 | clear-blue-sky/evolai-reborn-tfm-002 @
2026-05-24 09:21:46 9d512cab2a9007b7d58a6ec4988e6ac869910be5 | hotkey 5GC7k2mkTKGF…
2026-05-24 09:21:46     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:21:46     Fetched 20 texts (20 indices)
2026-05-24 09:21:46    Ready:
2026-05-24 09:21:46 clear-blue-sky/evolai-reborn-tfm-010@a925485d558b5b141050fd8bc943880e4a97b289
2026-05-24 09:21:46    Downloading
2026-05-24 09:21:46 mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678…
2026-05-24 09:21:48     Loaded (local prefetch)
2026-05-24 09:21:48     Model 0.46B → batch=512, seq=16384
2026-05-24 09:21:50    Ready: mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678
2026-05-24 09:22:26     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:22:26     Loss 3.7879 | Size ×0.50 | Think 3.7879 | ThinkGain 0 (+0.4573) | Flow
2026-05-24 09:22:26 0.3815 | KL 1.8789 | NextKL 1.7107 | SideQ 0% | Score 0.0000 (37.8s)
2026-05-24 09:22:26     Gate FAIL | Improve same SHA cur=1.8789 req<=1.8413 prev=1.8789 | Consist ok
2026-05-24 09:22:26 ema_cur=1.8935 ema_next=1.8746 ratio=0.990 max<=1.20
2026-05-24 09:22:28   Evicted cached model:
2026-05-24 09:22:28 Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0
2026-05-24 09:22:28   [13/50] UID 72 | clear-blue-sky/evolai-reborn-tfm-010 @
2026-05-24 09:22:28 a925485d558b5b141050fd8bc943880e4a97b289 | hotkey 5H3rMcqJQcbK…
2026-05-24 09:22:28     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:22:28     Fetched 20 texts (20 indices)
2026-05-24 09:22:28    Downloading
2026-05-24 09:22:28 mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a…
2026-05-24 09:22:30     Loaded (local prefetch)
2026-05-24 09:22:30     Model 0.46B → batch=512, seq=16384
2026-05-24 09:22:32    Ready: mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a
2026-05-24 09:23:08     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:23:09     Loss 3.7489 | Size ×0.50 | Think 3.7489 | ThinkGain 0 (+0.4588) | Flow
2026-05-24 09:23:09 0.1154 | KL 1.9608 | NextKL 1.9615 | SideQ 0% | Score 0.0000 (38.2s)
2026-05-24 09:23:09     Gate FAIL | Improve same SHA cur=1.9608 req<=1.9216 prev=1.9608 | Consist ok
2026-05-24 09:23:09 ema_cur=1.8872 ema_next=1.9113 ratio=1.013 max<=1.20
2026-05-24 09:23:10   Evicted cached model:
2026-05-24 09:23:10 evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a
2026-05-24 09:23:11   [14/50] UID 42 | mihai-777/evolai-tfm-1p5b-v5 @
2026-05-24 09:23:11 bd42aeb0828dfa0126f7fc825e13b49209fec678 | hotkey 5C5WCYnsrXRz…
2026-05-24 09:23:11     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:23:11    Downloading
2026-05-24 09:23:11 andrebarrosilva1123/evolai-e@806394ca7f2f7c1edbe962a9471647f4d67b5e72…
2026-05-24 09:23:11     Fetched 20 texts (20 indices)
2026-05-24 09:23:12     Loaded (local prefetch)
2026-05-24 09:23:13     Model 0.46B → batch=512, seq=16384
2026-05-24 09:23:17    Ready: andrebarrosilva1123/evolai-e@806394ca7f2f7c1edbe962a9471647f4d67b5e72
2026-05-24 09:23:51     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:23:52     Loss 2.7587 | Size ×0.50 | Think 2.7587 | ThinkGain 0 (+0.4553) | Flow
2026-05-24 09:23:52 0.2323 | KL 2.3318 | NextKL 2.2778 | SideQ 0% | Score 0.0000 (38.7s)
2026-05-24 09:23:52     Gate FAIL | Improve same SHA cur=2.3318 req<=2.2852 prev=2.3318 | Consist ok
2026-05-24 09:23:52 ema_cur=2.4267 ema_next=2.4233 ratio=0.999 max<=1.20
2026-05-24 09:23:53   Evicted cached model:
2026-05-24 09:23:53 mrthor102/evolai-tfm-super-003@75d4671ce2bf769be9ded4bd4205abef791212d1
2026-05-24 09:23:54   [15/50] UID 75 | mihai-777/evolai-tfm-1p5b-04 @
2026-05-24 09:23:54 fb289dbfe35c595b1a586f786a19e118cc1bfc9a | hotkey 5Dnz76SAsEv8…
2026-05-24 09:23:54     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:23:54     Fetched 20 texts (20 indices)
2026-05-24 09:23:54    Downloading
2026-05-24 09:23:54 clear-blue-sky/evolai-reborn-tfm-006@8c0b26d62d13ade4af1eaeea5967245266f27921…
2026-05-24 09:23:55     Loaded (local prefetch)
2026-05-24 09:23:55     Model 0.46B → batch=512, seq=16384
2026-05-24 09:23:59    Ready:
2026-05-24 09:23:59 clear-blue-sky/evolai-reborn-tfm-006@8c0b26d62d13ade4af1eaeea5967245266f27921
2026-05-24 09:24:34     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:24:34     Loss 3.1222 | Size ×0.50 | Think 3.1222 | ThinkGain 0 (+0.4513) | Flow
2026-05-24 09:24:34 0.2391 | KL 2.3897 | NextKL 2.7150 | SideQ 0% | Score 0.0000 (38.7s)
2026-05-24 09:24:34     Gate FAIL | Improve same SHA cur=2.3897 req<=2.3419 prev=2.3897 | Consist ok
2026-05-24 09:24:34 ema_cur=2.3391 ema_next=2.3922 ratio=1.023 max<=1.20
2026-05-24 09:24:36   Evicted cached model:
2026-05-24 09:24:36 clear-blue-sky/evolai-reborn-tfm-011@3c6fb9eda1f125661a5c6e9f4243ace37e38e4b5
2026-05-24 09:24:37   [16/50] UID 53 | andrebarrosilva1123/evolai-e @
2026-05-24 09:24:37 806394ca7f2f7c1edbe962a9471647f4d67b5e72 | hotkey 5EFgFa93M5Vx…
2026-05-24 09:24:37     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:24:37     Fetched 20 texts (20 indices)
2026-05-24 09:24:37    Downloading
2026-05-24 09:24:37 Radiant28/evolai-transformer-0.4b-b1@18231d7d50096d8b2744fdff1b38a7b90246ddf0…
2026-05-24 09:24:39     Loaded (local prefetch)
2026-05-24 09:24:40     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:24:42   [17/50] UID 66 | clear-blue-sky/evolai-reborn-tfm-006 @
2026-05-24 09:24:42 8c0b26d62d13ade4af1eaeea5967245266f27921 | hotkey 5E4M4B5sVED5…
2026-05-24 09:24:42     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:24:42     Fetched 20 texts (20 indices)
2026-05-24 09:24:44    Ready:
2026-05-24 09:24:44 Radiant28/evolai-transformer-0.4b-b1@18231d7d50096d8b2744fdff1b38a7b90246ddf0
2026-05-24 09:24:44    Downloading
2026-05-24 09:24:44 clear-blue-sky/evolai-reborn-tfm-007@75e0277bd4a5c60cc06a210fa9d5a05561356ef9…
2026-05-24 09:24:44     Loaded (local prefetch)
2026-05-24 09:24:44 Fetching 7 files: 100%|██████████| 7/7 [00:04<00:00,  1.46it/s]
2026-05-24 09:24:44     Model 0.46B → batch=512, seq=16384
2026-05-24 09:24:49    Ready:
2026-05-24 09:24:49 clear-blue-sky/evolai-reborn-tfm-007@75e0277bd4a5c60cc06a210fa9d5a05561356ef9
2026-05-24 09:25:24     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 09:25:24     Loss 4.0215 | Size ×0.50 | Think 4.0215 | ThinkGain 0 (+0.4613) | Flow
2026-05-24 09:25:24 0.0000 | KL 2.1556 | NextKL 1.7661 | SideQ 0% | Score 0.0000 (39.5s)
2026-05-24 09:25:24     Gate FAIL | Improve same SHA cur=2.1556 req<=2.1125 prev=2.1556 | Consist ok
2026-05-24 09:25:24 ema_cur=1.9865 ema_next=1.9590 ratio=0.986 max<=1.20
2026-05-24 09:25:26   Evicted cached model:
2026-05-24 09:25:26 mrthor102/evolai-tfm-super-002@db9483fdd7fb46c99ba8731900ec009330f4e77e
2026-05-24 09:25:26   [18/50] UID 35 | Radiant28/evolai-transformer-0.4b-b1 @
2026-05-24 09:25:26 18231d7d50096d8b2744fdff1b38a7b90246ddf0 | hotkey 5EXZBq3wQzTK…
2026-05-24 09:25:26     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:25:26     Fetched 20 texts (20 indices)
2026-05-24 09:25:26    Downloading Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600…
2026-05-24 09:25:28     Loaded (local prefetch)
2026-05-24 09:25:29     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:25:29    Ready: Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600
2026-05-24 09:25:31   [19/50] UID 84 | clear-blue-sky/evolai-reborn-tfm-007 @
2026-05-24 09:25:31 75e0277bd4a5c60cc06a210fa9d5a05561356ef9 | hotkey 5H1DaT8Dtt4N…
2026-05-24 09:25:31     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:25:31     Fetched 20 texts (20 indices)
2026-05-24 09:25:31    Downloading
2026-05-24 09:25:31 clear-blue-sky/evolai-reborn-tfm-003@8ec7e0ac5234f745104d4288bc15caf873d6a618…
2026-05-24 09:25:33     Loaded (local prefetch)
2026-05-24 09:25:33     Model 0.46B → batch=512, seq=16384
2026-05-24 09:25:35    Ready:
2026-05-24 09:25:35 clear-blue-sky/evolai-reborn-tfm-003@8ec7e0ac5234f745104d4288bc15caf873d6a618
2026-05-24 09:26:09     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:33
2026-05-24 09:26:09     Loss 4.0279 | Size ×0.50 | Think 4.0279 | ThinkGain 0 (+0.4607) | Flow
2026-05-24 09:26:09 0.0000 | KL 1.9723 | NextKL 1.9541 | SideQ 0% | Score 0.0000 (36.2s)
2026-05-24 09:26:09     Gate FAIL | Improve same SHA cur=1.9723 req<=1.9329 prev=1.9723 | Consist ok
2026-05-24 09:26:09 ema_cur=1.9474 ema_next=1.9672 ratio=1.010 max<=1.20
2026-05-24 09:26:12   Evicted cached model:
2026-05-24 09:26:12 mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c
2026-05-24 09:26:12   [20/50] UID 79 | Lin2es/evolai-tfm-03o @
2026-05-24 09:26:12 2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600 | hotkey 5D4eNqXRjWmX…
2026-05-24 09:26:12     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:26:12     Fetched 20 texts (20 indices)
2026-05-24 09:26:12    Downloading
2026-05-24 09:26:12 mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba…
2026-05-24 09:26:13     Loaded (local prefetch)
2026-05-24 09:26:13     Model 0.46B → batch=512, seq=16384
2026-05-24 09:26:16    Ready: mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba
2026-05-24 09:26:52     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:26:52     Loss 2.1565 | Size ×0.50 | Think 2.1565 | ThinkGain 0 (+0.4592) | Flow
2026-05-24 09:26:52 0.0000 | KL 2.7448 | NextKL 2.2582 | SideQ 0% | Score 0.0000 (38.4s)
2026-05-24 09:26:52     Gate FAIL | Improve same SHA cur=2.7448 req<=2.6899 prev=2.7448 | Consist ok
2026-05-24 09:26:52 ema_cur=2.4622 ema_next=2.4446 ratio=0.993 max<=1.20
2026-05-24 09:26:54   Evicted cached model:
2026-05-24 09:26:54 mrthor102/evolai-tfm-super-001@c2dac74023c984bf5261f93f33f748659f16f224
2026-05-24 09:26:54   [21/50] UID 82 | clear-blue-sky/evolai-reborn-tfm-003 @
2026-05-24 09:26:54 8ec7e0ac5234f745104d4288bc15caf873d6a618 | hotkey 5EtDxpyqHywK…
2026-05-24 09:26:54     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:26:54     Fetched 20 texts (20 indices)
2026-05-24 09:26:54    Downloading
2026-05-24 09:26:54 dreamiii0406/evolai-0p47b-v1@fea2659bdf8bd35e5382c50e4857f1ab20f20262…
2026-05-24 09:26:56     Loaded (local prefetch)
2026-05-24 09:26:56     Model 0.46B → batch=512, seq=16384
2026-05-24 09:26:57    Ready: dreamiii0406/evolai-0p47b-v1@fea2659bdf8bd35e5382c50e4857f1ab20f20262
2026-05-24 09:27:35     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:27:35     Loss 3.8003 | Size ×0.50 | Think 3.8003 | ThinkGain 0 (+0.4595) | Flow
2026-05-24 09:27:35 0.2898 | KL 1.7884 | NextKL 1.7842 | SideQ 0% | Score 0.0000 (38.5s)
2026-05-24 09:27:35     Gate FAIL | Improve same SHA cur=1.7884 req<=1.7526 prev=1.7884 | Consist ok
2026-05-24 09:27:35 ema_cur=1.8791 ema_next=1.8924 ratio=1.007 max<=1.20
2026-05-24 09:27:36   Evicted cached model:
2026-05-24 09:27:36 clear-blue-sky/evolai-reborn-tfm-002@9d512cab2a9007b7d58a6ec4988e6ac869910be5
2026-05-24 09:27:38   [22/50] UID 76 | mihai-777/evolai-tfm-1p5b-05 @
2026-05-24 09:27:38 a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba | hotkey 5GLBxPtoiB7R…
2026-05-24 09:27:38     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:27:38     Fetched 20 texts (20 indices)
2026-05-24 09:27:38    Downloading Radiant28/evolai-1p5b@e351598db6d77f85b5081768df04d37c132750f0…
2026-05-24 09:27:39     Loaded (local prefetch)
2026-05-24 09:27:39     Model 0.46B → batch=512, seq=16384
2026-05-24 09:27:44    Ready: Radiant28/evolai-1p5b@e351598db6d77f85b5081768df04d37c132750f0
2026-05-24 09:28:18     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:28:18     Loss 3.2388 | Size ×0.50 | Think 3.2388 | ThinkGain 0 (+0.4559) | Flow
2026-05-24 09:28:18 0.0255 | KL 2.4729 | NextKL 2.1805 | SideQ 0% | Score 0.0000 (38.7s)
2026-05-24 09:28:18     Gate FAIL | Improve same SHA cur=2.4729 req<=2.4235 prev=2.4729 | Consist ok
2026-05-24 09:28:18 ema_cur=2.4511 ema_next=2.4083 ratio=0.983 max<=1.20
2026-05-24 09:28:19   Evicted cached model:
2026-05-24 09:28:19 clear-blue-sky/evolai-reborn-tfm-010@a925485d558b5b141050fd8bc943880e4a97b289
2026-05-24 09:28:20   [23/50] UID 80 | dreamiii0406/evolai-0p47b-v1 @
2026-05-24 09:28:20 fea2659bdf8bd35e5382c50e4857f1ab20f20262 | hotkey 5Cd2zZyMQnvp…
2026-05-24 09:28:20     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:28:20     Fetched 20 texts (20 indices)
2026-05-24 09:28:20    Downloading
2026-05-24 09:28:20 mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a…
2026-05-24 09:28:22     Loaded (local prefetch)
2026-05-24 09:28:22     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:28:24   [24/50] UID 43 | Radiant28/evolai-1p5b @
2026-05-24 09:28:24 e351598db6d77f85b5081768df04d37c132750f0 | hotkey 5HSz4knZnWHY…
2026-05-24 09:28:24     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:28:24     Fetched 20 texts (20 indices)
2026-05-24 09:28:24    Ready: mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a
2026-05-24 09:28:24    Downloading
2026-05-24 09:28:24 mrthor102/evolai-tfm-super-004@6623560efa96f6a92a6b9557dcf0e2b1ae0391cc…
2026-05-24 09:28:26     Loaded (local prefetch)
2026-05-24 09:28:27     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:28:28    Ready:
2026-05-24 09:28:28 mrthor102/evolai-tfm-super-004@6623560efa96f6a92a6b9557dcf0e2b1ae0391cc
2026-05-24 09:28:29   [25/50] UID 38 | mihai-777/evolai-tfm-1p5b-alt @
2026-05-24 09:28:29 5ebb4a406916abe39e32823ff1f635b70e707e5a | hotkey 5FbfiXysyCtC…
2026-05-24 09:28:29     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:28:29     Fetched 20 texts (20 indices)
2026-05-24 09:28:29    Downloading
2026-05-24 09:28:29 Radiant28/evolai-0.4b-V1@5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5…
2026-05-24 09:28:30     Loaded (local prefetch)
2026-05-24 09:28:31     Model 0.46B → batch=512, seq=16384
2026-05-24 09:28:35    Ready: Radiant28/evolai-0.4b-V1@5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5
2026-05-24 09:29:09     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:29:10     Loss 3.3879 | Size ×0.50 | Think 3.3879 | ThinkGain 0 (+0.4532) | Flow
2026-05-24 09:29:10 0.1063 | KL 2.4928 | NextKL 2.7254 | SideQ 0% | Score 0.0000 (38.7s)
2026-05-24 09:29:10     Gate FAIL | Improve same SHA cur=2.4928 req<=2.4429 prev=2.4928 | Consist ok
2026-05-24 09:29:10 ema_cur=2.3842 ema_next=2.4343 ratio=1.021 max<=1.20
2026-05-24 09:29:11   Evicted cached model:
2026-05-24 09:29:11 mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678
2026-05-24 09:29:12   [26/50] UID 99 | mrthor102/evolai-tfm-super-004 @
2026-05-24 09:29:12 6623560efa96f6a92a6b9557dcf0e2b1ae0391cc | hotkey 5EnuPuwNaqmP…
2026-05-24 09:29:12    Downloading evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4…
2026-05-24 09:29:12     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:29:12     Fetched 20 texts (20 indices)
2026-05-24 09:29:13     Loaded (local prefetch)
2026-05-24 09:29:13     Model 0.46B → batch=512, seq=16384
2026-05-24 09:29:14    Ready: evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4
2026-05-24 09:29:53     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 09:29:53     Loss 3.9796 | Size ×0.50 | Think 3.9796 | ThinkGain 0 (+0.4601) | Flow
2026-05-24 09:29:53 0.0000 | KL 2.0584 | NextKL 1.8793 | SideQ 0% | Score 0.0000 (39.2s)
2026-05-24 09:29:53     Gate FAIL | Improve same SHA cur=2.0584 req<=2.0172 prev=2.0584 | Consist ok
2026-05-24 09:29:53 ema_cur=1.9689 ema_next=1.9558 ratio=0.993 max<=1.20
2026-05-24 09:29:55   Evicted cached model:
2026-05-24 09:29:55 mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a
2026-05-24 09:29:55   [27/50] UID 44 | Radiant28/evolai-0.4b-V1 @
2026-05-24 09:29:55 5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5 | hotkey 5DXm2ShZGmwG…
2026-05-24 09:29:55     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:29:55    Downloading philk11/evolai-0.4b@822950352d63cdd145c3a7449ebfd4b51ad5ae6a…
2026-05-24 09:29:55     Fetched 20 texts (20 indices)
2026-05-24 09:29:57     Loaded (local prefetch)
2026-05-24 09:29:58     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:29:59    Ready: philk11/evolai-0.4b@822950352d63cdd145c3a7449ebfd4b51ad5ae6a
2026-05-24 09:30:00   [28/50] UID 95 | evolai/evolai_naive_kl @
2026-05-24 09:30:00 da8203b6900f14ec1b724f3dd8c6dc35576fc3e4 | hotkey 5CXwmm7R4U6o…
2026-05-24 09:30:00     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:30:00     Fetched 20 texts (20 indices)
2026-05-24 09:30:00    Downloading
2026-05-24 09:30:00 Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9…
2026-05-24 09:30:01     Loaded (local prefetch)
2026-05-24 09:30:02     Model 0.46B → batch=512, seq=16384
2026-05-24 09:30:04    Ready: Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9
2026-05-24 09:30:41     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 09:30:41     Loss 2.5589 | Size ×0.50 | Think 2.5589 | ThinkGain 0 (+0.4842) | Flow
2026-05-24 09:30:41 0.1349 | KL 2.7039 | NextKL 2.0342 | SideQ 0% | Score 0.0000 (39.3s)
2026-05-24 09:30:41     Gate FAIL | Improve same SHA cur=2.7039 req<=2.6498 prev=2.7039 | Consist ok
2026-05-24 09:30:41 ema_cur=2.8320 ema_next=2.7384 ratio=0.967 max<=1.20
2026-05-24 09:30:43   Evicted cached model:
2026-05-24 09:30:43 clear-blue-sky/evolai-reborn-tfm-006@8c0b26d62d13ade4af1eaeea5967245266f27921
2026-05-24 09:30:43   [29/50] UID 65 | philk11/evolai-0.4b @
2026-05-24 09:30:43 822950352d63cdd145c3a7449ebfd4b51ad5ae6a | hotkey 5GvHE1tHbhGv…
2026-05-24 09:30:43     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:30:43     Fetched 20 texts (20 indices)
2026-05-24 09:30:43    Downloading
2026-05-24 09:30:43 andrebarrosilva1123/evolai-f@89654c7b1e351cce36bab65fe09692eb0e109f72…
2026-05-24 09:30:45     Loaded (local prefetch)
2026-05-24 09:30:45     ⚠ Invalid model size (0.60B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 09:30:47   [30/50] UID 93 | Phoenix9781/evolai-tf-model @
2026-05-24 09:30:47 b05038fcfdcc79fa8d8e79730074b65cd68c73f9 | hotkey 5F4R25t78FSF…
2026-05-24 09:30:47     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:30:47     Fetched 20 texts (20 indices)
2026-05-24 09:30:49     Loaded (local prefetch)
2026-05-24 09:30:49     Model 0.46B → batch=512, seq=16384
2026-05-24 09:30:50    Ready: andrebarrosilva1123/evolai-f@89654c7b1e351cce36bab65fe09692eb0e109f72
2026-05-24 09:30:50    Downloading
2026-05-24 09:30:50 clear-blue-sky/evolai-reborn-tfm-004@2921306430562eff35ea2c11aabd1b9412e19961…
2026-05-24 09:30:50 Fetching 7 files: 100%|██████████| 7/7 [00:04<00:00,  1.65it/s]
2026-05-24 09:30:54    Ready:
2026-05-24 09:30:54 clear-blue-sky/evolai-reborn-tfm-004@2921306430562eff35ea2c11aabd1b9412e19961
2026-05-24 09:31:27     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 09:31:27     Loss 3.3512 | Size ×0.50 | Think 3.3512 | ThinkGain 0 (+0.4606) | Flow
2026-05-24 09:31:27 0.0000 | KL 1.9957 | NextKL 2.0425 | SideQ 0% | Score 0.0000 (37.6s)
2026-05-24 09:31:27     Gate FAIL | Improve same SHA cur=1.9957 req<=1.9558 prev=1.9957 | Consist ok
2026-05-24 09:31:27 ema_cur=1.9758 ema_next=1.9750 ratio=1.000 max<=1.20
2026-05-24 09:31:28   Evicted cached model:
2026-05-24 09:31:28 clear-blue-sky/evolai-reborn-tfm-007@75e0277bd4a5c60cc06a210fa9d5a05561356ef9
2026-05-24 09:31:29   [31/50] UID 52 | andrebarrosilva1123/evolai-f @
2026-05-24 09:31:29 89654c7b1e351cce36bab65fe09692eb0e109f72 | hotkey 5HTZZEb5oxv9…
2026-05-24 09:31:29     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:31:29     Fetched 20 texts (20 indices)
2026-05-24 09:31:29    Downloading
2026-05-24 09:31:29 evolai/evolai_test_challenge@71d0f7058e451a387164d5b4497cda29481578ca…
2026-05-24 09:31:31     Loaded (local prefetch)
2026-05-24 09:31:32     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:31:33    Ready: evolai/evolai_test_challenge@71d0f7058e451a387164d5b4497cda29481578ca
2026-05-24 09:31:34   [32/50] UID 70 | clear-blue-sky/evolai-reborn-tfm-004 @
2026-05-24 09:31:34 2921306430562eff35ea2c11aabd1b9412e19961 | hotkey 5Hdg2gHopWQK…
2026-05-24 09:31:34     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:31:34     Fetched 20 texts (20 indices)
2026-05-24 09:31:34    Downloading
2026-05-24 09:31:34 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb…
2026-05-24 09:31:35     Loaded (local prefetch)
2026-05-24 09:31:36     Model 0.46B → batch=512, seq=16384
2026-05-24 09:31:38    Ready:
2026-05-24 09:31:38 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb
2026-05-24 09:32:14     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:32:14     Loss 3.8439 | Size ×0.50 | Think 3.8439 | ThinkGain 0 (+0.4646) | Flow
2026-05-24 09:32:14 0.0000 | KL 1.9566 | NextKL 1.9589 | SideQ 0% | Score 0.0000 (38.4s)
2026-05-24 09:32:14     Gate FAIL | Improve same SHA cur=1.9566 req<=1.9175 prev=1.9566 | Consist ok
2026-05-24 09:32:14 ema_cur=1.9088 ema_next=1.9155 ratio=1.004 max<=1.20
2026-05-24 09:32:16   Evicted cached model:
2026-05-24 09:32:16 Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600
2026-05-24 09:32:17   [33/50] UID 8 | evolai/evolai_test_challenge @
2026-05-24 09:32:17 71d0f7058e451a387164d5b4497cda29481578ca | hotkey 5ENhqnBoyFdz…
2026-05-24 09:32:17     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:32:17     Fetched 20 texts (20 indices)
2026-05-24 09:32:17    Downloading
2026-05-24 09:32:17 Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002…
2026-05-24 09:32:18     Loaded (local prefetch)
2026-05-24 09:32:18     Model 0.46B → batch=512, seq=16384
2026-05-24 09:32:20    Ready: Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002
2026-05-24 09:32:57     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:32:58     Loss 3.9201 | Size ×0.50 | Think 3.9201 | ThinkGain 0 (+0.4530) | Flow
2026-05-24 09:32:58 0.0000 | KL 2.0210 | NextKL 1.9705 | SideQ 0% | Score 0.0000 (38.9s)
2026-05-24 09:32:58     Gate FAIL | Improve same SHA cur=2.0210 req<=1.9806 prev=2.0210 | Consist ok
2026-05-24 09:32:58 ema_cur=1.7650 ema_next=1.9547 ratio=1.107 max<=1.20
2026-05-24 09:32:59   Evicted cached model:
2026-05-24 09:32:59 clear-blue-sky/evolai-reborn-tfm-003@8ec7e0ac5234f745104d4288bc15caf873d6a618
2026-05-24 09:33:00   [34/50] UID 48 | sangerno63/evolai-transformer-v2 @
2026-05-24 09:33:00 4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb | hotkey 5ED3KNj5uEVS…
2026-05-24 09:33:00     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:33:00     Fetched 20 texts (20 indices)
2026-05-24 09:33:00    Downloading Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d…
2026-05-24 09:33:01     Loaded (local prefetch)
2026-05-24 09:33:02     Model 0.46B → batch=512, seq=16384
2026-05-24 09:33:03    Ready: Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d
2026-05-24 09:33:41     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 76/76 100% 0:00:35
2026-05-24 09:33:41     Loss 3.9755 | Size ×0.50 | Think 3.9755 | ThinkGain 0 (+0.4428) | Flow
2026-05-24 09:33:41 0.1188 | KL 2.2343 | NextKL 2.0905 | SideQ 3% | Score 0.0001 (38.8s)
2026-05-24 09:33:41     Gate FAIL | Improve same SHA cur=2.2343 req<=2.1896 prev=2.2343 | Consist ok
2026-05-24 09:33:41 ema_cur=2.1939 ema_next=2.1759 ratio=0.992 max<=1.20
2026-05-24 09:33:42   Evicted cached model:
2026-05-24 09:33:42 mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba
2026-05-24 09:33:43   [35/50] UID 100 | Danieli1021/evolai-qwen047-v3 @
2026-05-24 09:33:43 e01dfd3b9c54325c98bf12966bdebadace391002 | hotkey 5DMH2VrrukYd…
2026-05-24 09:33:43     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:33:43     Fetched 20 texts (20 indices)
2026-05-24 09:33:43    Downloading galuis116/evolai-future@7591e0441945f1ba85f2e78d6239cee711a66dce…
2026-05-24 09:33:44     Loaded (local prefetch)
2026-05-24 09:33:45     Model 0.47B → batch=512, seq=16384
2026-05-24 09:33:47    Ready: galuis116/evolai-future@7591e0441945f1ba85f2e78d6239cee711a66dce
2026-05-24 09:34:04     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:16
2026-05-24 09:34:04     Loss 4.2818 | Size ×0.51 | Think 4.2818 | ThinkGain 0 (+0.4805) | Flow
2026-05-24 09:34:04 0.0000 | KL 3.8850 | NextKL 3.9174 | SideQ 0% | Score 0.0000 (19.2s)
2026-05-24 09:34:04     Gate FAIL | Improve same SHA cur=3.8850 req<=3.8073 prev=3.8850 | Consist ok
2026-05-24 09:34:04 ema_cur=4.3911 ema_next=3.9306 ratio=0.895 max<=1.20
2026-05-24 09:34:05   Evicted cached model:
2026-05-24 09:34:05 mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a
2026-05-24 09:34:06   [36/50] UID 77 | Lin2es/evolai-tfm-01o @
2026-05-24 09:34:06 d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d | hotkey 5GQydjNVEhMb…
2026-05-24 09:34:06     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:34:06     Fetched 20 texts (20 indices)
2026-05-24 09:34:06    Downloading
2026-05-24 09:34:06 clear-blue-sky/evolai-reborn-tfm-009@8e9182e3c2d2a51341f6b7ad8f9f9b4c9405ae24…
2026-05-24 09:34:08     Loaded (local prefetch)
2026-05-24 09:34:08     Model 0.46B → batch=512, seq=16384
2026-05-24 09:34:10    Ready:
2026-05-24 09:34:10 clear-blue-sky/evolai-reborn-tfm-009@8e9182e3c2d2a51341f6b7ad8f9f9b4c9405ae24
2026-05-24 09:34:46     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 09:34:46     Loss 2.1268 | Size ×0.50 | Think 2.1268 | ThinkGain 0 (+0.4347) | Flow
2026-05-24 09:34:46 0.0326 | KL 2.3210 | NextKL 2.1894 | SideQ 0% | Score 0.0000 (37.9s)
2026-05-24 09:34:46     Gate FAIL | Improve same SHA cur=2.3210 req<=2.2745 prev=2.3210 | Consist ok
2026-05-24 09:34:46 ema_cur=2.5927 ema_next=2.5343 ratio=0.978 max<=1.20
2026-05-24 09:34:47   Evicted cached model:
2026-05-24 09:34:47 mrthor102/evolai-tfm-super-004@6623560efa96f6a92a6b9557dcf0e2b1ae0391cc
2026-05-24 09:34:48   [37/50] UID 101 | galuis116/evolai-future @
2026-05-24 09:34:48 7591e0441945f1ba85f2e78d6239cee711a66dce | hotkey 5DPz76uobJLT…
2026-05-24 09:34:48     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:34:48     Fetched 20 texts (20 indices)
2026-05-24 09:34:48    Downloading
2026-05-24 09:34:48 andrebarrosilva1123/evolai-d@89649e9376dace64f631711d3d270198e376702e…
2026-05-24 09:34:50     Loaded (local prefetch)
2026-05-24 09:34:50     Model 0.46B → batch=512, seq=16384
2026-05-24 09:34:55    Ready: andrebarrosilva1123/evolai-d@89649e9376dace64f631711d3d270198e376702e
2026-05-24 09:35:29     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:35:29     Loss 3.8113 | Size ×0.50 | Think 3.8113 | ThinkGain 0 (+0.4582) | Flow
2026-05-24 09:35:29 0.4366 | KL 1.6579 | NextKL 1.8845 | SideQ 0% | Score 0.0000 (38.6s)
2026-05-24 09:35:29     Gate FAIL | Improve same SHA cur=1.6579 req<=1.6248 prev=1.6579 | Consist ok
2026-05-24 09:35:29 ema_cur=1.8685 ema_next=1.8699 ratio=1.001 max<=1.20
2026-05-24 09:35:31   Evicted cached model:
2026-05-24 09:35:31 evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4
2026-05-24 09:35:31   [38/50] UID 69 | clear-blue-sky/evolai-reborn-tfm-009 @
2026-05-24 09:35:31 8e9182e3c2d2a51341f6b7ad8f9f9b4c9405ae24 | hotkey 5ChUCf3NjrgS…
2026-05-24 09:35:31     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:35:31     Fetched 20 texts (20 indices)
2026-05-24 09:35:31    Downloading
2026-05-24 09:35:31 andrebarrosilva1123/evolai-c@6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c…
2026-05-24 09:35:32     Loaded (local prefetch)
2026-05-24 09:35:33     Model 0.46B → batch=512, seq=16384
2026-05-24 09:35:37    Ready: andrebarrosilva1123/evolai-c@6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c
2026-05-24 09:36:12     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 09:36:12     Loss 3.5552 | Size ×0.50 | Think 3.5552 | ThinkGain 0 (+0.4605) | Flow
2026-05-24 09:36:12 0.3767 | KL 1.8861 | NextKL 2.1831 | SideQ 0% | Score 0.0000 (38.9s)
2026-05-24 09:36:12     Gate FAIL | Improve same SHA cur=1.8861 req<=1.8484 prev=1.8861 | Consist ok
2026-05-24 09:36:12 ema_cur=1.9000 ema_next=1.9324 ratio=1.017 max<=1.20
2026-05-24 09:36:14   Evicted cached model:
2026-05-24 09:36:14 Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9
2026-05-24 09:36:14   [39/50] UID 51 | andrebarrosilva1123/evolai-d @
2026-05-24 09:36:14 89649e9376dace64f631711d3d270198e376702e | hotkey 5EhLiPB1GHwH…
2026-05-24 09:36:14     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:36:14     Fetched 20 texts (20 indices)
2026-05-24 09:36:14    Downloading
2026-05-24 09:36:14 Roystar/evolai-qwen2.5-1.5b@47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1…
2026-05-24 09:36:16     Loaded (local prefetch)
2026-05-24 09:36:17     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:36:19   [40/50] UID 54 | andrebarrosilva1123/evolai-c @
2026-05-24 09:36:19 6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c | hotkey 5D7HPRR2QdDB…
2026-05-24 09:36:19     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:36:19     Fetched 20 texts (20 indices)
2026-05-24 09:36:21    Ready: Roystar/evolai-qwen2.5-1.5b@47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1
2026-05-24 09:36:21    Downloading Jubilant/evolai-1.54b@d8681d30b14cb5a597d2ff7c909998cf9d217599…
2026-05-24 09:36:21     Loaded (local prefetch)
2026-05-24 09:36:21 Fetching 7 files: 100%|██████████| 7/7 [00:05<00:00,  1.22it/s]
2026-05-24 09:36:21     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:36:24   [41/50] UID 55 | Roystar/evolai-qwen2.5-1.5b @
2026-05-24 09:36:24 47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1 | hotkey 5DhRJtUeVA6P…
2026-05-24 09:36:24     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:36:24     Fetched 20 texts (20 indices)
2026-05-24 09:36:26     Loaded (local prefetch)
2026-05-24 09:36:26     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:36:27    Ready: Jubilant/evolai-1.54b@d8681d30b14cb5a597d2ff7c909998cf9d217599
2026-05-24 09:36:27    Downloading Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59…
2026-05-24 09:36:29   [42/50] UID 36 | Jubilant/evolai-1.54b @
2026-05-24 09:36:29 d8681d30b14cb5a597d2ff7c909998cf9d217599 | hotkey 5G7Co5VNfQio…
2026-05-24 09:36:29     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:36:29     Fetched 20 texts (20 indices)
2026-05-24 09:36:29 Fetching 7 files: 100%|██████████| 7/7 [00:02<00:00,  3.06it/s]
2026-05-24 09:36:31     Loaded (local prefetch)
2026-05-24 09:36:31    Ready: Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59
2026-05-24 09:36:31    Downloading
2026-05-24 09:36:31 clear-blue-sky/evolai-reborn-tfm-001@5233a721363395c7abfdcfad299f43520b003100…
2026-05-24 09:36:31 Fetching 7 files: 100%|██████████| 7/7 [00:04<00:00,  1.73it/s]
2026-05-24 09:36:31     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:36:33   [43/50] UID 78 | Lin2es/evolai-tfm-02o @
2026-05-24 09:36:33 fc5fc3ee4a3877b825b404dc85c9367c1f248c59 | hotkey 5FA2kgLNs36d…
2026-05-24 09:36:33     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:36:33     Fetched 20 texts (20 indices)
2026-05-24 09:36:35     Loaded (local prefetch)
2026-05-24 09:36:35     Model 0.46B → batch=512, seq=16384
2026-05-24 09:36:35    Ready:
2026-05-24 09:36:35 clear-blue-sky/evolai-reborn-tfm-001@5233a721363395c7abfdcfad299f43520b003100
2026-05-24 09:36:35    Downloading
2026-05-24 09:36:35 Jubilant/evolai-1.50b-v1@074810c41bab77c52a216e0c2f7886484e12deeb…
2026-05-24 09:36:35 Fetching 7 files: 100%|██████████| 7/7 [00:05<00:00,  1.23it/s]
2026-05-24 09:36:41    Ready: Jubilant/evolai-1.50b-v1@074810c41bab77c52a216e0c2f7886484e12deeb
2026-05-24 09:37:14     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:37:14     Loss 2.9847 | Size ×0.50 | Think 2.9847 | ThinkGain 0 (+0.4272) | Flow
2026-05-24 09:37:14 0.0125 | KL 2.5967 | NextKL 3.0763 | SideQ 0% | Score 0.0000 (38.9s)
2026-05-24 09:37:14     Gate FAIL | Improve same SHA cur=2.5967 req<=2.5447 prev=2.5967 | Consist ok
2026-05-24 09:37:14 ema_cur=2.7868 ema_next=2.8127 ratio=1.009 max<=1.20
2026-05-24 09:37:16   Evicted cached model:
2026-05-24 09:37:16 clear-blue-sky/evolai-reborn-tfm-004@2921306430562eff35ea2c11aabd1b9412e19961
2026-05-24 09:37:16   [44/50] UID 62 | clear-blue-sky/evolai-reborn-tfm-001 @
2026-05-24 09:37:16 5233a721363395c7abfdcfad299f43520b003100 | hotkey 5EjjVuNJsjqP…
2026-05-24 09:37:16     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:37:16    Downloading
2026-05-24 09:37:16 dexserbia/evolai-gemma2-9b@7fe66309a3847239a4da5b712477f2105e88399b…
2026-05-24 09:37:16     Fetched 20 texts (20 indices)
2026-05-24 09:37:18     Loaded (local prefetch)
2026-05-24 09:37:18     Model 0.46B → batch=512, seq=16384
2026-05-24 09:37:46    Ready: dexserbia/evolai-gemma2-9b@7fe66309a3847239a4da5b712477f2105e88399b
2026-05-24 09:37:58     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:37
2026-05-24 09:37:58     Loss 3.3079 | Size ×0.50 | Think 3.3079 | ThinkGain 0 (+0.4592) | Flow
2026-05-24 09:37:58 0.0000 | KL 1.9640 | NextKL 1.9541 | SideQ 0% | Score 0.0000 (40.0s)
2026-05-24 09:37:58     Gate FAIL | Improve same SHA cur=1.9640 req<=1.9247 prev=1.9640 | Consist ok
2026-05-24 09:37:58 ema_cur=1.9482 ema_next=1.9305 ratio=0.991 max<=1.20
2026-05-24 09:38:00   Evicted cached model:
2026-05-24 09:38:00 evolai/evolai_test_challenge@71d0f7058e451a387164d5b4497cda29481578ca
2026-05-24 09:38:00   [45/50] UID 40 | Jubilant/evolai-1.50b-v1 @
2026-05-24 09:38:00 074810c41bab77c52a216e0c2f7886484e12deeb | hotkey 5Fuv43yR7tjJ…
2026-05-24 09:38:00     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:38:00     Fetched 20 texts (20 indices)
2026-05-24 09:38:00    Downloading
2026-05-24 09:38:00 clear-blue-sky/evolai-reborn-tfm-005@455b69e426e6ca0721b3f69943223fe21173d569…
2026-05-24 09:38:02     Loaded (local prefetch)
2026-05-24 09:38:02     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:38:04   [46/50] UID 9 | dexserbia/evolai-gemma2-9b @
2026-05-24 09:38:04 7fe66309a3847239a4da5b712477f2105e88399b | hotkey 5EbpxBkVKVNV…
2026-05-24 09:38:04     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:38:04     Fetched 20 texts (20 indices)
2026-05-24 09:38:04    Ready:
2026-05-24 09:38:04 clear-blue-sky/evolai-reborn-tfm-005@455b69e426e6ca0721b3f69943223fe21173d569
2026-05-24 09:38:04    Downloading Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4…
2026-05-24 09:38:07    Ready: Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4
2026-05-24 09:38:09     Loaded (local prefetch)
2026-05-24 09:38:11     ⚠ Invalid model size (9.24B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 09:38:13   [47/50] UID 83 | clear-blue-sky/evolai-reborn-tfm-005 @
2026-05-24 09:38:13 455b69e426e6ca0721b3f69943223fe21173d569 | hotkey 5G8tRiKdn5cC…
2026-05-24 09:38:13     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:38:13     Fetched 20 texts (20 indices)
2026-05-24 09:38:13    Downloading
2026-05-24 09:38:13 batster4/evolai-phi4-mini-dpo-v1@8217794abaf74f8e15f578a507e27b5f9b1df4c9…
2026-05-24 09:38:15     Loaded (local prefetch)
2026-05-24 09:38:15     Model 0.46B → batch=512, seq=16384
2026-05-24 09:38:27    Ready:
2026-05-24 09:38:27 batster4/evolai-phi4-mini-dpo-v1@8217794abaf74f8e15f578a507e27b5f9b1df4c9
2026-05-24 09:38:55     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 09:38:55     Loss 3.6630 | Size ×0.50 | Think 3.6630 | ThinkGain 0 (+0.4615) | Flow
2026-05-24 09:38:55 0.0000 | KL 2.0068 | NextKL 1.8505 | SideQ 0% | Score 0.0000 (39.7s)
2026-05-24 09:38:55     Gate FAIL | Improve same SHA cur=2.0068 req<=1.9666 prev=2.0068 | Consist ok
2026-05-24 09:38:55 ema_cur=2.5401 ema_next=1.9367 ratio=0.762 max<=1.20
2026-05-24 09:38:57   Evicted cached model:
2026-05-24 09:38:57 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb
2026-05-24 09:38:57   [48/50] UID 92 | Lin2es/evolai-tfm-04o @
2026-05-24 09:38:57 52061d203723fdc8be09324d0c827898fcb7bdc4 | hotkey 5GefYX69KUVQ…
2026-05-24 09:38:57     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:38:57     Fetched 20 texts (20 indices)
2026-05-24 09:38:57    Downloading
2026-05-24 09:38:57 clear-blue-sky/evolai-reborn-tfm-008@819b51083eb5f5e01d1a1e50c836daf868e0f1e7…
2026-05-24 09:38:59     Loaded (local prefetch)
2026-05-24 09:38:59     Model 0.46B → batch=512, seq=16384
2026-05-24 09:39:03    Ready:
2026-05-24 09:39:03 clear-blue-sky/evolai-reborn-tfm-008@819b51083eb5f5e01d1a1e50c836daf868e0f1e7
2026-05-24 09:39:37     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:39:37     Loss 2.4308 | Size ×0.50 | Think 2.4308 | ThinkGain 0 (+0.4456) | Flow
2026-05-24 09:39:37 0.0000 | KL 2.5771 | NextKL 2.6527 | SideQ 0% | Score 0.0000 (38.2s)
2026-05-24 09:39:37     Gate FAIL | Improve same SHA cur=2.5771 req<=2.5255 prev=2.5771 | Consist ok
2026-05-24 09:39:37 ema_cur=3.0519 ema_next=2.5399 ratio=0.832 max<=1.20
2026-05-24 09:39:39   Evicted cached model:
2026-05-24 09:39:39 Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002
2026-05-24 09:39:40   [49/50] UID 59 | batster4/evolai-phi4-mini-dpo-v1 @
2026-05-24 09:39:40 8217794abaf74f8e15f578a507e27b5f9b1df4c9 | hotkey 5GCA2s6m4RRM…
2026-05-24 09:39:40     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:39:40     Fetched 20 texts (20 indices)
2026-05-24 09:39:42     Loaded (local prefetch)
2026-05-24 09:39:43     ⚠ Invalid model size (3.84B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 09:39:45   [50/50] UID 85 | clear-blue-sky/evolai-reborn-tfm-008 @
2026-05-24 09:39:45 819b51083eb5f5e01d1a1e50c836daf868e0f1e7 | hotkey 5EC5MzPj6dGb…
2026-05-24 09:39:45     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:39:45     Fetched 20 texts (20 indices)
2026-05-24 09:39:47     Loaded (local prefetch)
2026-05-24 09:39:47     Model 0.46B → batch=512, seq=16384
2026-05-24 09:40:25     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 09:40:25     Loss 3.9013 | Size ×0.50 | Think 3.9013 | ThinkGain 0 (+0.4609) | Flow
2026-05-24 09:40:25 0.0000 | KL 1.8934 | NextKL 1.8427 | SideQ 0% | Score 0.0000 (37.4s)
2026-05-24 09:40:25     Gate FAIL | Improve same SHA cur=1.8934 req<=1.8555 prev=1.8934 | Consist ok
2026-05-24 09:40:25 ema_cur=2.5321 ema_next=1.9471 ratio=0.769 max<=1.20
2026-05-24 09:40:26   Evicted cached model:
2026-05-24 09:40:26 Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d
2026-05-24 09:40:27   Cached next refs for transformer: 50 miner(s)
2026-05-24 09:40:27 
2026-05-24 09:40:27   ✓ TRANSFORMER: 30 evaluated, 23 skipped —
2026-05-24 09:40:27 epoch_22924_transformer_20260524_091333.json
2026-05-24 09:40:28   ✓ Telemetry sent (30 records)
2026-05-24 09:40:28 Evaluating MAMBA2 track…
2026-05-24 09:40:28 
2026-05-24 09:40:28   Found 15 locked mamba2 miners
2026-05-24 09:40:28    Downloading Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8…
2026-05-24 09:40:28 Pre-building current/next challenges for 15 miners…
2026-05-24 09:40:28 Fetching 7 files: 100%|██████████| 7/7 [00:02<00:00,  2.63it/s]
2026-05-24 09:40:30    Ready: Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8
2026-05-24 09:40:30    Downloading
2026-05-24 09:40:30 elgin-group/evolai-mamba2-0p47b-v1@39b2f90ad08643d34503c88f5c7224fd3dabeed7…
2026-05-24 09:40:31 Fetching 8 files: 100%|██████████| 8/8 [00:03<00:00,  2.57it/s]
2026-05-24 09:40:34    Ready:
2026-05-24 09:40:34 elgin-group/evolai-mamba2-0p47b-v1@39b2f90ad08643d34503c88f5c7224fd3dabeed7
2026-05-24 09:40:48 ✓ Ref data ready: submitted=15, cached=15
2026-05-24 09:40:48   [1/15] UID 90 | Lin2es/evolai-mb2-02v @
2026-05-24 09:40:48 c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8 | hotkey 5CtLLhrw6Lxa…
2026-05-24 09:40:48     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:40:48     Fetched 20 texts (20 indices)
2026-05-24 09:40:48    Downloading
2026-05-24 09:40:48 andrebarrosilva1123/evolai-mamba2-a@55b92d373b1c219a4cfbac7034c154ddbcdc854d…
2026-05-24 09:40:50     Loaded (local prefetch)
2026-05-24 09:40:50     Model 0.48B → batch=512, seq=16384
2026-05-24 09:40:51    Ready:
2026-05-24 09:40:51 andrebarrosilva1123/evolai-mamba2-a@55b92d373b1c219a4cfbac7034c154ddbcdc854d
2026-05-24 09:41:00     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:03
2026-05-24 09:41:01     Loss 4.6426 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:41:01 0.0000 | KL 4.6426 | NextKL 4.7207 | SideQ 0% | Score 0.0000 (10.5s)
2026-05-24 09:41:01     Gate FAIL | Improve same SHA cur=4.6426 req<=4.5497 prev=4.6426 | Consist ok
2026-05-24 09:41:01 ema_cur=5.0934 ema_next=4.7092 ratio=0.925 max<=1.20
2026-05-24 09:41:02   Evicted cached model:
2026-05-24 09:41:02 galuis116/evolai-future@7591e0441945f1ba85f2e78d6239cee711a66dce
2026-05-24 09:41:03   [2/15] UID 34 | elgin-group/evolai-mamba2-0p47b-v1 @
2026-05-24 09:41:03 39b2f90ad08643d34503c88f5c7224fd3dabeed7 | hotkey 5GNJr9NfE9e9…
2026-05-24 09:41:03     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:41:03     Fetched 20 texts (20 indices)
2026-05-24 09:41:03    Downloading
2026-05-24 09:41:03 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c…
2026-05-24 09:41:06     Loaded (local prefetch)
2026-05-24 09:41:06     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 09:41:07    Ready:
2026-05-24 09:41:07 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c
2026-05-24 09:41:08   [3/15] UID 56 | andrebarrosilva1123/evolai-mamba2-a @
2026-05-24 09:41:08 55b92d373b1c219a4cfbac7034c154ddbcdc854d | hotkey 5D1zGn2n3mzF…
2026-05-24 09:41:08     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:41:08     Fetched 20 texts (20 indices)
2026-05-24 09:41:08    Downloading
2026-05-24 09:41:08 andrebarrosilva1123/evolai-mamba2-b@62336a49df6d6014f779575adfd29373c228edd4…
2026-05-24 09:41:11    Ready:
2026-05-24 09:41:11 andrebarrosilva1123/evolai-mamba2-b@62336a49df6d6014f779575adfd29373c228edd4
2026-05-24 09:41:12     Loaded (local prefetch)
2026-05-24 09:41:13     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 09:41:15   [4/15] UID 32 | mihai-777/evolai-mamba2-1p6b-alt @
2026-05-24 09:41:15 131bd3907f9816bbf184f5651ba63af66046e84c | hotkey 5GL84HKDau7C…
2026-05-24 09:41:15     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:41:15    Downloading
2026-05-24 09:41:15 Radiant28/evolai-mamba2-0.47b-v3@97f692fb0b295aa29075d3f9d592bfb4e7625b16…
2026-05-24 09:41:15     Fetched 20 texts (20 indices)
2026-05-24 09:41:17     Loaded (local prefetch)
2026-05-24 09:41:17     Model 0.48B → batch=512, seq=16384
2026-05-24 09:41:18    Ready:
2026-05-24 09:41:18 Radiant28/evolai-mamba2-0.47b-v3@97f692fb0b295aa29075d3f9d592bfb4e7625b16
2026-05-24 09:41:22     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:02
2026-05-24 09:41:22     Loss 4.8477 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:41:22 0.0318 | KL 4.8477 | NextKL 4.8405 | SideQ 0% | Score 0.0000 (5.3s)
2026-05-24 09:41:22     Gate FAIL | Improve same SHA cur=4.8477 req<=4.7508 prev=4.8477 | Consist ok
2026-05-24 09:41:22 ema_cur=4.8841 ema_next=4.8709 ratio=0.997 max<=1.20
2026-05-24 09:41:24   Evicted cached model:
2026-05-24 09:41:24 clear-blue-sky/evolai-reborn-tfm-009@8e9182e3c2d2a51341f6b7ad8f9f9b4c9405ae24
2026-05-24 09:41:24   [5/15] UID 57 | andrebarrosilva1123/evolai-mamba2-b @
2026-05-24 09:41:24 62336a49df6d6014f779575adfd29373c228edd4 | hotkey 5EZx1DRvpMGK…
2026-05-24 09:41:24     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:41:24    Downloading Lin2es/evolai-mb2-04v@9c0198682f16cc8595fec849aa37227f7160e92c…
2026-05-24 09:41:24     Fetched 20 texts (20 indices)
2026-05-24 09:41:26     Loaded (local prefetch)
2026-05-24 09:41:26     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 09:41:27    Ready: Lin2es/evolai-mb2-04v@9c0198682f16cc8595fec849aa37227f7160e92c
2026-05-24 09:41:28   [6/15] UID 41 | Radiant28/evolai-mamba2-0.47b-v3 @
2026-05-24 09:41:28 97f692fb0b295aa29075d3f9d592bfb4e7625b16 | hotkey 5CP5QrWuFe93…
2026-05-24 09:41:28     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:41:28    Downloading
2026-05-24 09:41:28 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518…
2026-05-24 09:41:28     Fetched 20 texts (20 indices)
2026-05-24 09:41:29     Loaded (local prefetch)
2026-05-24 09:41:29     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 09:41:31   [7/15] UID 89 | Lin2es/evolai-mb2-04v @
2026-05-24 09:41:31 9c0198682f16cc8595fec849aa37227f7160e92c | hotkey 5DkZf6V3X8Za…
2026-05-24 09:41:31     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:41:31     Fetched 20 texts (20 indices)
2026-05-24 09:41:31    Ready:
2026-05-24 09:41:31 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518
2026-05-24 09:41:31    Downloading Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd…
2026-05-24 09:41:33     Loaded (local prefetch)
2026-05-24 09:41:33     ⚠ Vocab incompatible (model=151665 < ref=248077) — skipping
2026-05-24 09:41:34    Ready: Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd
2026-05-24 09:41:35   [8/15] UID 30 | mihai-777/evolai-mamba2-0p47b-v3 @
2026-05-24 09:41:35 c2a96b92acf632d51a2c21da4482f77f98256518 | hotkey 5GGsbuVKDrTA…
2026-05-24 09:41:35     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:41:35     Fetched 20 texts (20 indices)
2026-05-24 09:41:35    Downloading
2026-05-24 09:41:35 mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7…
2026-05-24 09:41:36     Loaded (local prefetch)
2026-05-24 09:41:37     Model 0.48B → batch=512, seq=16384
2026-05-24 09:41:38    Ready: mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7
2026-05-24 09:41:41     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 09:41:41     Loss 4.7301 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:41:41 0.1887 | KL 4.7301 | NextKL 4.5888 | SideQ 0% | Score 0.0000 (4.1s)
2026-05-24 09:41:41     Gate FAIL | Improve same SHA cur=4.7301 req<=4.6355 prev=4.7301 | Consist ok
2026-05-24 09:41:41 ema_cur=4.7890 ema_next=4.7742 ratio=0.997 max<=1.20
2026-05-24 09:41:43   Evicted cached model:
2026-05-24 09:41:43 Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59
2026-05-24 09:41:43   [9/15] UID 91 | Lin2es/evolai-mb2-03v @
2026-05-24 09:41:43 3047597c4e4b4430450ddcd633240b88d781fdbd | hotkey 5EcdUqvUBCSp…
2026-05-24 09:41:43     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:41:43     Fetched 20 texts (20 indices)
2026-05-24 09:41:43    Downloading Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0…
2026-05-24 09:41:45     Loaded (local prefetch)
2026-05-24 09:41:45     Model 0.48B → batch=512, seq=16384
2026-05-24 09:41:46    Ready: Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0
2026-05-24 09:41:49     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 09:41:49     Loss 4.6332 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:41:49 0.0000 | KL 4.6332 | NextKL 4.6708 | SideQ 0% | Score 0.0000 (4.3s)
2026-05-24 09:41:49     Gate FAIL | Improve same SHA cur=4.6332 req<=4.5405 prev=4.6332 | Consist ok
2026-05-24 09:41:49 ema_cur=4.6643 ema_next=4.6678 ratio=1.001 max<=1.20
2026-05-24 09:41:51   Evicted cached model:
2026-05-24 09:41:51 clear-blue-sky/evolai-reborn-tfm-001@5233a721363395c7abfdcfad299f43520b003100
2026-05-24 09:41:52   [10/15] UID 31 | mihai-777/evolai-mamba2-0p47b @
2026-05-24 09:41:52 7b6564c9a46f602702c260185aa43867f321dee7 | hotkey 5CJuKKq16FkR…
2026-05-24 09:41:52     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:41:52     Fetched 20 texts (20 indices)
2026-05-24 09:41:52    Downloading
2026-05-24 09:41:52 andrebarrosilva1123/evolai-mamba2-c@dc37c985d66c77e3d10bf9eaf16e6dc952c62e17…
2026-05-24 09:41:53     Loaded (local prefetch)
2026-05-24 09:41:53     Model 0.48B → batch=512, seq=16384
2026-05-24 09:41:55    Ready:
2026-05-24 09:41:55 andrebarrosilva1123/evolai-mamba2-c@dc37c985d66c77e3d10bf9eaf16e6dc952c62e17
2026-05-24 09:41:57     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 09:41:57     Loss 4.7761 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:41:57 0.0000 | KL 4.7761 | NextKL 4.8005 | SideQ 0% | Score 0.0000 (3.7s)
2026-05-24 09:41:57     Gate FAIL | Improve same SHA cur=4.7761 req<=4.6806 prev=4.7761 | Consist ok
2026-05-24 09:41:57 ema_cur=4.7754 ema_next=4.7731 ratio=1.000 max<=1.20
2026-05-24 09:41:58   Evicted cached model:
2026-05-24 09:41:58 clear-blue-sky/evolai-reborn-tfm-005@455b69e426e6ca0721b3f69943223fe21173d569
2026-05-24 09:41:59   [11/15] UID 11 | Lin2es/evolai-mb2-01v @
2026-05-24 09:41:59 a7f32e5ce7f8d307c98560e5025525f3703310c0 | hotkey 5HYuS4jrJJ56…
2026-05-24 09:41:59    Downloading
2026-05-24 09:41:59 evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a…
2026-05-24 09:41:59     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:41:59     Fetched 20 texts (20 indices)
2026-05-24 09:42:01     Loaded (local prefetch)
2026-05-24 09:42:01     Model 0.48B → batch=512, seq=16384
2026-05-24 09:42:02    Ready: evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a
2026-05-24 09:42:05     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 09:42:05     Loss 4.7182 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:42:05 0.0479 | KL 4.7182 | NextKL 4.7112 | SideQ 0% | Score 0.0000 (4.0s)
2026-05-24 09:42:05     Gate FAIL | Improve same SHA cur=4.7182 req<=4.6239 prev=4.7182 | Consist ok
2026-05-24 09:42:05 ema_cur=4.6567 ema_next=4.6699 ratio=1.003 max<=1.20
2026-05-24 09:42:07   Evicted cached model:
2026-05-24 09:42:07 Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4
2026-05-24 09:42:07   [12/15] UID 58 | andrebarrosilva1123/evolai-mamba2-c @
2026-05-24 09:42:07 dc37c985d66c77e3d10bf9eaf16e6dc952c62e17 | hotkey 5EgtSzXJbjpV…
2026-05-24 09:42:07     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:42:07     Fetched 20 texts (20 indices)
2026-05-24 09:42:07    Downloading
2026-05-24 09:42:07 Radiant28/evolai-mamba2-0.47b-v2@475bf7bf65af1192ed824d58816c1d83f3475983…
2026-05-24 09:42:09     Loaded (local prefetch)
2026-05-24 09:42:09     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 09:42:10    Ready:
2026-05-24 09:42:10 Radiant28/evolai-mamba2-0.47b-v2@475bf7bf65af1192ed824d58816c1d83f3475983
2026-05-24 09:42:11   [13/15] UID 96 | evolai/evolai_mamba_naive_kl @
2026-05-24 09:42:11 b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a | hotkey 5HQuJVXBXGrW…
2026-05-24 09:42:11     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:42:11     Fetched 20 texts (20 indices)
2026-05-24 09:42:11    Downloading
2026-05-24 09:42:11 batster4/evolai-mamba2-v1@142f14d218be618e3161d86926085b3a9cefed55…
2026-05-24 09:42:12     Loaded (local prefetch)
2026-05-24 09:42:12     Model 0.46B → batch=512, seq=16384
2026-05-24 09:42:14    Ready: batster4/evolai-mamba2-v1@142f14d218be618e3161d86926085b3a9cefed55
2026-05-24 09:42:16     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 09:42:16     Loss 3.1070 | Size ×0.50 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 09:42:16 0.0000 | KL 3.1070 | NextKL 3.5648 | SideQ 0% | Score 0.0000 (3.8s)
2026-05-24 09:42:16     Gate FAIL | Improve same SHA cur=3.1070 req<=3.0449 prev=3.1070 | Consist ok
2026-05-24 09:42:16 ema_cur=3.9336 ema_next=3.4756 ratio=0.884 max<=1.20
2026-05-24 09:42:18   Evicted cached model:
2026-05-24 09:42:18 clear-blue-sky/evolai-reborn-tfm-008@819b51083eb5f5e01d1a1e50c836daf868e0f1e7
2026-05-24 09:42:18   [14/15] UID 39 | Radiant28/evolai-mamba2-0.47b-v2 @
2026-05-24 09:42:18 475bf7bf65af1192ed824d58816c1d83f3475983 | hotkey 5FvTt3gVVhFT…
2026-05-24 09:42:18     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:42:18     Fetched 20 texts (20 indices)
2026-05-24 09:42:20     Loaded (local prefetch)
2026-05-24 09:42:20     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 09:42:22   [15/15] UID 60 | batster4/evolai-mamba2-v1 @
2026-05-24 09:42:22 142f14d218be618e3161d86926085b3a9cefed55 | hotkey 5Dc8EpAixcqc…
2026-05-24 09:42:22     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:42:22     Fetched 20 texts (20 indices)
2026-05-24 09:42:23     Loaded (local prefetch)
2026-05-24 09:42:23     ⚠ Invalid model size (0.82B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 09:42:25   Cached next refs for mamba2: 15 miner(s)
2026-05-24 09:42:25 
2026-05-24 09:42:25   ✓ MAMBA2: 7 evaluated, 14 skipped — epoch_22924_mamba2_20260524_091333.json
2026-05-24 09:42:25   ✓ Telemetry sent (7 records)
2026-05-24 09:42:25 Current Leaderboard:
2026-05-24 09:42:40 
2026-05-24 09:42:40 TRANSFORMER
2026-05-24 09:42:40 ┏━━━━━━┳━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━━━┳━━━━━━━┓
2026-05-24 09:42:40 ┃      ┃     ┃        ┃     Latest ┃           ┃       ┃     ┃         ┃       ┃
2026-05-24 09:42:40 ┃ Rank ┃ UID ┃  Score ┃       Loss ┃ ThinkGain ┃  Flow ┃ SQ% ┃      KL ┃ Evals ┃
2026-05-24 09:42:40 ┡━━━━━━╇━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━━━╇━━━━━━━┩
2026-05-24 09:42:40 │    1 │  48 │ 0.0001 │     3.9755 │  0 FAIL   │ 0.119 │  3% │  2.2343 │   133 │
2026-05-24 09:42:40 │    2 │  82 │ 0.0000 │     3.8003 │  0 FAIL   │ 0.290 │  0% │  1.7884 │   344 │
2026-05-24 09:42:40 │    3 │  66 │ 0.0000 │     4.0215 │  0 FAIL   │ 0.000 │  0% │  2.1556 │   344 │
2026-05-24 09:42:40 │    4 │  87 │ 0.0000 │     4.0577 │  0 FAIL   │ 0.133 │  0% │  2.2495 │   147 │
2026-05-24 09:42:40 │    5 │  86 │ 0.0000 │     4.1094 │  0 FAIL   │ 0.139 │  0% │  2.3171 │   148 │
2026-05-24 09:42:40 │    6 │  73 │ 0.0000 │     3.8881 │  0 FAIL   │ 0.000 │  0% │  1.7976 │   129 │
2026-05-24 09:42:40 │    7 │  93 │ 0.0000 │     3.3512 │  0 FAIL   │ 0.000 │  0% │  1.9957 │   129 │
2026-05-24 09:42:40 │    8 │  97 │ 0.0000 │     3.7057 │  0 FAIL   │ 0.000 │  0% │  2.0417 │   259 │
2026-05-24 09:42:40 │    9 │  67 │ 0.0000 │     3.7879 │  0 FAIL   │ 0.381 │  0% │  1.8789 │   346 │
2026-05-24 09:42:40 │   10 │  70 │ 0.0000 │     3.8439 │  0 FAIL   │ 0.000 │  0% │  1.9566 │   344 │
2026-05-24 09:42:40 │   11 │  83 │ 0.0000 │     3.6630 │  0 FAIL   │ 0.000 │  0% │  2.0068 │   346 │
2026-05-24 09:42:40 │   12 │  85 │ 0.0000 │     3.9013 │  0 FAIL   │ 0.000 │  0% │  1.8934 │   333 │
2026-05-24 09:42:40 │   13 │  99 │ 0.0000 │     3.9796 │  0 FAIL   │ 0.000 │  0% │  2.0584 │   127 │
2026-05-24 09:42:40 │   14 │  72 │ 0.0000 │     3.7489 │  0 FAIL   │ 0.115 │  0% │  1.9608 │   128 │
2026-05-24 09:42:40 │   15 │  62 │ 0.0000 │     3.3079 │  0 FAIL   │ 0.000 │  0% │  1.9640 │   346 │
2026-05-24 09:42:40 │   16 │  94 │ 0.0000 │     3.6372 │  0 FAIL   │ 0.118 │  0% │  1.6471 │   259 │
2026-05-24 09:42:40 │   17 │   8 │ 0.0000 │     3.9201 │  0 FAIL   │ 0.000 │  0% │  2.0210 │   309 │
2026-05-24 09:42:40 │   18 │  98 │ 0.0000 │     4.0643 │  0 FAIL   │ 0.074 │  0% │  1.8700 │   258 │
2026-05-24 09:42:40 │   19 │  69 │ 0.0000 │     3.5552 │  0 FAIL   │ 0.377 │  0% │  1.8861 │   129 │
2026-05-24 09:42:40 │   20 │   9 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 09:42:40 │   21 │  25 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:42:40 │   22 │  33 │ 0.0000 │     2.4238 │  0 FAIL   │ 0.063 │  0% │  2.2523 │   346 │
2026-05-24 09:42:40 │   23 │  35 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 09:42:40 │   24 │  36 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:42:40 │   25 │  37 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 09:42:40 │   26 │  38 │ 0.0000 │     3.3879 │  0 FAIL   │ 0.106 │  0% │  2.4928 │   345 │
2026-05-24 09:42:40 │   27 │  40 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 09:42:40 │   28 │  42 │ 0.0000 │     2.7587 │  0 FAIL   │ 0.232 │  0% │  2.3318 │   346 │
2026-05-24 09:42:40 │   29 │  43 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 09:42:40 │   30 │  44 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 09:42:40 │   31 │  45 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 09:42:40 │   32 │  49 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:42:40 │   33 │  50 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 09:42:40 │   34 │  51 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   318 │
2026-05-24 09:42:40 │   35 │  52 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   319 │
2026-05-24 09:42:40 │   36 │  53 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 09:42:40 │   37 │  54 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   317 │
2026-05-24 09:42:40 │   38 │  55 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   349 │
2026-05-24 09:42:40 │   39 │  59 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 09:42:40 │   40 │  61 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 09:42:40 │   41 │  65 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 09:42:40 │   42 │  75 │ 0.0000 │     3.1222 │  0 FAIL   │ 0.239 │  0% │  2.3897 │   347 │
2026-05-24 09:42:40 │   43 │  76 │ 0.0000 │     3.2388 │  0 FAIL   │ 0.025 │  0% │  2.4729 │   345 │
2026-05-24 09:42:40 │   44 │  77 │ 0.0000 │     2.1268 │  0 FAIL   │ 0.033 │  0% │  2.3210 │   248 │
2026-05-24 09:42:40 │   45 │  78 │ 0.0000 │     2.9847 │  0 FAIL   │ 0.012 │  0% │  2.5967 │   248 │
2026-05-24 09:42:40 │   46 │  79 │ 0.0000 │     2.1565 │  0 FAIL   │ 0.000 │  0% │  2.7448 │   248 │
2026-05-24 09:42:40 │   47 │  80 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 09:42:40 │   48 │  84 │ 0.0000 │     4.0279 │  0 FAIL   │ 0.000 │  0% │  1.9723 │   330 │
2026-05-24 09:42:40 │   49 │  88 │ 0.0000 │     3.9147 │  0 FAIL   │ 0.290 │  0% │  1.9992 │   146 │
2026-05-24 09:42:40 │   50 │  92 │ 0.0000 │     2.4308 │  0 FAIL   │ 0.000 │  0% │  2.5771 │   249 │
2026-05-24 09:42:40 │   51 │  95 │ 0.0000 │     2.5589 │  0 FAIL   │ 0.135 │  0% │  2.7039 │   258 │
2026-05-24 09:42:40 │   52 │ 100 │ 0.0000 │     4.2818 │  0 FAIL   │ 0.000 │  0% │  3.8850 │   257 │
2026-05-24 09:42:40 │   53 │ 101 │ 0.0000 │     3.8113 │  0 FAIL   │ 0.437 │  0% │  1.6579 │    79 │
2026-05-24 09:42:40 └──────┴─────┴────────┴────────────┴───────────┴───────┴─────┴─────────┴───────┘
2026-05-24 09:42:40 
2026-05-24 09:42:40 MAMBA2
2026-05-24 09:42:40 ┏━━━━━━┳━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━━━┳━━━━━━━┓
2026-05-24 09:42:40 ┃      ┃     ┃        ┃     Latest ┃           ┃       ┃     ┃         ┃       ┃
2026-05-24 09:42:40 ┃ Rank ┃ UID ┃  Score ┃       Loss ┃ ThinkGain ┃  Flow ┃ SQ% ┃      KL ┃ Evals ┃
2026-05-24 09:42:40 ┡━━━━━━╇━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━━━╇━━━━━━━┩
2026-05-24 09:42:40 │    1 │  11 │ 0.0000 │     4.7182 │  0 FAIL   │ 0.048 │  0% │  4.7182 │   248 │
2026-05-24 09:42:40 │    2 │  30 │ 0.0000 │     4.7301 │  0 FAIL   │ 0.189 │  0% │  4.7301 │   343 │
2026-05-24 09:42:40 │    3 │  31 │ 0.0000 │     4.7761 │  0 FAIL   │ 0.000 │  0% │  4.7761 │   343 │
2026-05-24 09:42:40 │    4 │  32 │ 0.0000 │     4.8477 │  0 FAIL   │ 0.032 │  0% │  4.8477 │   343 │
2026-05-24 09:42:40 │    5 │  34 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   343 │
2026-05-24 09:42:40 │    6 │  39 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 09:42:40 │    7 │  41 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   343 │
2026-05-24 09:42:40 │    8 │  56 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   343 │
2026-05-24 09:42:40 │    9 │  57 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   343 │
2026-05-24 09:42:40 │   10 │  58 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   343 │
2026-05-24 09:42:40 │   11 │  60 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   343 │
2026-05-24 09:42:40 │   12 │  63 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   271 │
2026-05-24 09:42:40 │   13 │  64 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 09:42:40 │   14 │  68 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 09:42:40 │   15 │  71 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   271 │
2026-05-24 09:42:40 │   16 │  74 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 09:42:40 │   17 │  81 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   273 │
2026-05-24 09:42:40 │   18 │  89 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   248 │
2026-05-24 09:42:40 │   19 │  90 │ 0.0000 │     4.6426 │  0 FAIL   │ 0.000 │  0% │  4.6426 │   258 │
2026-05-24 09:42:40 │   20 │  91 │ 0.0000 │     4.6332 │  0 FAIL   │ 0.000 │  0% │  4.6332 │   258 │
2026-05-24 09:42:40 │   21 │  96 │ 0.0000 │     3.1070 │  0 FAIL   │ 0.000 │  0% │  3.1070 │   258 │
2026-05-24 09:42:40 └──────┴─────┴────────┴────────────┴───────────┴───────┴─────┴─────────┴───────┘
2026-05-24 09:42:40 
2026-05-24 09:42:40 Round complete in epoch 22924 (1747s elapsed). Starting next round immediately…
2026-05-24 09:42:40 
2026-05-24 09:42:40 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2026-05-24 09:42:40 
2026-05-24 09:42:40 ━━━ Epoch #22925 (Loop #4) ━━━ block=8253124, ~47m remaining
2026-05-24 09:42:50 
2026-05-24 09:42:50   ⚠ UID 86: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:42:50 (Request ID:
2026-05-24 09:42:50 Root=1-6a12c81a-52627dac56b2e224487b88a2;ea67f031-a0e6-4f7f-a855-9ceb428b7746)
2026-05-24 09:42:50 
2026-05-24 09:42:50 Repository Not Found for url:
2026-05-24 09:42:50 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-012/revision/main.
2026-05-24 09:42:50 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:42:50 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:42:50 authenticated and your token has the required permissions.
2026-05-24 09:42:50 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:42:50 Invalid username or password.
2026-05-24 09:42:50   ⚠ UID 87: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:42:50 (Request ID:
2026-05-24 09:42:50 Root=1-6a12c81a-381f67a47b251c947ecfe236;66742d54-32fe-4598-b513-8e0eb89fd019)
2026-05-24 09:42:50 
2026-05-24 09:42:50 Repository Not Found for url:
2026-05-24 09:42:50 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-013/revision/main.
2026-05-24 09:42:50 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:42:50 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:42:50 authenticated and your token has the required permissions.
2026-05-24 09:42:50 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:42:50 Invalid username or password.
2026-05-24 09:42:50   ⚠ UID 88: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:42:50 (Request ID:
2026-05-24 09:42:50 Root=1-6a12c81a-2b51915f65e8ab65156bb9f3;102de0b2-a7aa-4219-9f55-8e351e14ae34)
2026-05-24 09:42:50 
2026-05-24 09:42:50 Repository Not Found for url:
2026-05-24 09:42:50 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-014/revision/main.
2026-05-24 09:42:50 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:42:50 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:42:50 authenticated and your token has the required permissions.
2026-05-24 09:42:50 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:42:50 Invalid username or password.
2026-05-24 09:42:50   Locked transformer revisions (50 miner(s), 3 skipped)
2026-05-24 09:42:58   ⚠ UID 63: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:42:58 (Request ID:
2026-05-24 09:42:58 Root=1-6a12c822-669fb40c288a1b7f5689acf2;ed5242ae-0369-4f54-b0d4-13d5775f7b39)
2026-05-24 09:42:58 
2026-05-24 09:42:58 Repository Not Found for url:
2026-05-24 09:42:58 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-009/revision/main.
2026-05-24 09:42:58 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:42:58 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:42:58 authenticated and your token has the required permissions.
2026-05-24 09:42:58 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:42:58 Invalid username or password.
2026-05-24 09:42:58   ⚠ UID 64: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:42:58 (Request ID:
2026-05-24 09:42:58 Root=1-6a12c822-66054e9475c4de4d01e59a2b;ad4c2154-f97d-4a00-8e6f-8dce94aefcbd)
2026-05-24 09:42:58 
2026-05-24 09:42:58 Repository Not Found for url:
2026-05-24 09:42:58 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-002/revision/main.
2026-05-24 09:42:58 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:42:58 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:42:58 authenticated and your token has the required permissions.
2026-05-24 09:42:58 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:42:58 Invalid username or password.
2026-05-24 09:42:58   ⚠ UID 68: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:42:58 (Request ID:
2026-05-24 09:42:58 Root=1-6a12c822-3a79a821786b15a12a84bf2c;12e383ed-082c-4ab7-a0ea-275c0a9d8886)
2026-05-24 09:42:58 
2026-05-24 09:42:58 Repository Not Found for url:
2026-05-24 09:42:58 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-008/revision/main.
2026-05-24 09:42:58 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:42:58 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:42:58 authenticated and your token has the required permissions.
2026-05-24 09:42:58 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:42:58 Invalid username or password.
2026-05-24 09:42:58   ⚠ UID 71: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:42:58 (Request ID:
2026-05-24 09:42:58 Root=1-6a12c822-27ca4b5b0d255ff2555bdb13;a349221f-5b81-4f28-a3e4-a8c3d6b80421)
2026-05-24 09:42:58 
2026-05-24 09:42:58 Repository Not Found for url:
2026-05-24 09:42:58 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-001/revision/main.
2026-05-24 09:42:58 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:42:58 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:42:58 authenticated and your token has the required permissions.
2026-05-24 09:42:58 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:42:58 Invalid username or password.
2026-05-24 09:42:59   ⚠ UID 74: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:42:59 (Request ID:
2026-05-24 09:42:59 Root=1-6a12c822-69f274211073fbfc4c2ea7e2;b1f091df-f9f2-4f3d-a846-e182c2e8acdf)
2026-05-24 09:42:59 
2026-05-24 09:42:59 Repository Not Found for url:
2026-05-24 09:42:59 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-007/revision/main.
2026-05-24 09:42:59 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:42:59 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:42:59 authenticated and your token has the required permissions.
2026-05-24 09:42:59 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:42:59 Invalid username or password.
2026-05-24 09:42:59   ⚠ UID 81: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 09:42:59 (Request ID:
2026-05-24 09:42:59 Root=1-6a12c823-42d649db267401e90cfdd274;9f073448-775a-4deb-a2c2-658fee0ff82e)
2026-05-24 09:42:59 
2026-05-24 09:42:59 Repository Not Found for url:
2026-05-24 09:42:59 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-010/revision/main.
2026-05-24 09:42:59 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 09:42:59 If you are trying to access a private or gated repo, make sure you are
2026-05-24 09:42:59 authenticated and your token has the required permissions.
2026-05-24 09:42:59 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 09:42:59 Invalid username or password.
2026-05-24 09:42:59   Locked mamba2 revisions (15 miner(s), 6 skipped)
2026-05-24 09:43:27   Committed round seed epoch=22925 seed=e8e3fde3...
2026-05-24 09:43:28 Evaluating TRANSFORMER track…
2026-05-24 09:43:28 
2026-05-24 09:43:28   Found 50 locked transformer miners
2026-05-24 09:43:28    Downloading
2026-05-24 09:43:28 andrebarrosilva1123/evolai-0.4b@fa913c93aa7a7449066ce870427387bd3fc7e841…
2026-05-24 09:43:28 Pre-building current/next challenges for 50 miners…
2026-05-24 09:43:28 Fetching 7 files: 100%|██████████| 7/7 [00:06<00:00,  1.06it/s]
2026-05-24 09:43:32    alpha=0.005454 TAO/α  budget=0.049684
2026-05-24 09:43:35    Ready:
2026-05-24 09:43:35 andrebarrosilva1123/evolai-0.4b@fa913c93aa7a7449066ce870427387bd3fc7e841
2026-05-24 09:43:35    Downloading Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d…
2026-05-24 09:43:35 Fetching 7 files: 100%|██████████| 7/7 [00:03<00:00,  2.28it/s]
2026-05-24 09:43:38    Ready: Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d
2026-05-24 09:43:50    emission scale=1.000 (active miners)
2026-05-24 09:43:50    emission scale=1.000 (active miners)
2026-05-24 09:43:50    all quality scores zero after gates — emission share redistributed to
2026-05-24 09:43:50 productive tracks
2026-05-24 09:43:52   ✓  set at 09:43:52 UTC
2026-05-24 09:44:21 ✓ Ref data ready: submitted=50, cached=50
2026-05-24 09:44:21   [1/50] UID 49 | andrebarrosilva1123/evolai-0.4b @
2026-05-24 09:44:21 fa913c93aa7a7449066ce870427387bd3fc7e841 | hotkey 5DULz3AJEisH…
2026-05-24 09:44:21     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:44:21    Downloading
2026-05-24 09:44:21 clear-blue-sky/evolai-reborn-tfm-007@22d900793d1d3e4eff1eafd02c6767bd579ef7f2…
2026-05-24 09:44:21     Fetched 20 texts (20 indices)
2026-05-24 09:44:24     Loaded (local prefetch)
2026-05-24 09:44:24     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:44:27   [2/50] UID 77 | Lin2es/evolai-tfm-01o @
2026-05-24 09:44:27 d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d | hotkey 5GQydjNVEhMb…
2026-05-24 09:44:27     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:44:27     Fetched 20 texts (20 indices)
2026-05-24 09:44:27    Ready:
2026-05-24 09:44:27 clear-blue-sky/evolai-reborn-tfm-007@22d900793d1d3e4eff1eafd02c6767bd579ef7f2
2026-05-24 09:44:27    Downloading
2026-05-24 09:44:27 evolai/evolai_test_challenge@4f5368ca6af7b884196482aebe78f284ac8eec98…
2026-05-24 09:44:29     Loaded (local prefetch)
2026-05-24 09:44:29     Model 0.46B → batch=512, seq=16384
2026-05-24 09:44:31    Ready: evolai/evolai_test_challenge@4f5368ca6af7b884196482aebe78f284ac8eec98
2026-05-24 09:45:31     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:56
2026-05-24 09:45:32     Loss 1.6774 | Size ×0.50 | Think 1.6774 | ThinkGain 0 (+0.4320) | Flow
2026-05-24 09:45:32 0.1907 | KL 2.1894 | NextKL 2.9899 | SideQ 0% | Score 0.0000 (62.3s)
2026-05-24 09:45:32     Gate FAIL | Improve same SHA cur=2.1894 req<=2.1456 prev=2.1894 | Consist ok
2026-05-24 09:45:32 ema_cur=2.5523 ema_next=2.5799 ratio=1.011 max<=1.20
2026-05-24 09:45:33   Evicted cached model:
2026-05-24 09:45:33 Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8
2026-05-24 09:45:34   [3/50] UID 84 | clear-blue-sky/evolai-reborn-tfm-007 @
2026-05-24 09:45:34 22d900793d1d3e4eff1eafd02c6767bd579ef7f2 | hotkey 5H1DaT8Dtt4N…
2026-05-24 09:45:34     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:45:34    Downloading philk11/evolai-0.4b@822950352d63cdd145c3a7449ebfd4b51ad5ae6a…
2026-05-24 09:45:34     Fetched 20 texts (20 indices)
2026-05-24 09:45:36     Loaded (local prefetch)
2026-05-24 09:45:36     Model 0.46B → batch=512, seq=16384
2026-05-24 09:45:38    Ready: philk11/evolai-0.4b@822950352d63cdd145c3a7449ebfd4b51ad5ae6a
2026-05-24 09:46:30     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:51
2026-05-24 09:46:31     Loss 3.7483 | Size ×0.50 | Think 3.7483 | ThinkGain 0 (+0.4607) | Flow
2026-05-24 09:46:31 0.0000 | KL 1.9477 | NextKL 1.9309 | SideQ 0% | Score 0.0000 (54.3s)
2026-05-24 09:46:31     Gate FAIL | Improve FAIL cur=1.9477 req<=1.9150 prev=1.9541 | Consist ok
2026-05-24 09:46:31 ema_cur=1.9474 ema_next=1.9636 ratio=1.008 max<=1.20
2026-05-24 09:46:32   Evicted cached model:
2026-05-24 09:46:32 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c
2026-05-24 09:46:33   [4/50] UID 8 | evolai/evolai_test_challenge @
2026-05-24 09:46:33 4f5368ca6af7b884196482aebe78f284ac8eec98 | hotkey 5ENhqnBoyFdz…
2026-05-24 09:46:33     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:46:33     Fetched 20 texts (20 indices)
2026-05-24 09:46:33    Downloading
2026-05-24 09:46:33 Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002…
2026-05-24 09:46:36     Loaded (local prefetch)
2026-05-24 09:46:37     Model 0.46B → batch=512, seq=16384
2026-05-24 09:46:38    Ready: Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002
2026-05-24 09:47:36     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:55
2026-05-24 09:47:36     Loss 3.8183 | Size ×0.50 | Think 3.8183 | ThinkGain 0 (+0.4544) | Flow
2026-05-24 09:47:36 0.0000 | KL 1.7714 | NextKL 1.8511 | SideQ 0% | Score 0.0302 (58.8s)
2026-05-24 09:47:36     Gate PASS | Improve ok cur=1.7714 req<=1.9311 prev=1.9705 | Consist ok
2026-05-24 09:47:36 ema_cur=1.7657 ema_next=1.9443 ratio=1.101 max<=1.20
2026-05-24 09:47:37   Evicted cached model:
2026-05-24 09:47:37 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518
2026-05-24 09:47:38   [5/50] UID 65 | philk11/evolai-0.4b @ 822950352d63cdd145c3a7449ebfd4b51ad5ae6a
2026-05-24 09:47:38 | hotkey 5GvHE1tHbhGv…
2026-05-24 09:47:38     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:47:38     Fetched 20 texts (20 indices)
2026-05-24 09:47:38    Downloading
2026-05-24 09:47:38 Radiant28/evolai-0.4b-V1@5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5…
2026-05-24 09:47:40     Loaded (local prefetch)
2026-05-24 09:47:40     ⚠ Invalid model size (0.60B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 09:47:42   [6/50] UID 100 | Danieli1021/evolai-qwen047-v3 @
2026-05-24 09:47:42 e01dfd3b9c54325c98bf12966bdebadace391002 | hotkey 5DMH2VrrukYd…
2026-05-24 09:47:42     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:47:42     Fetched 20 texts (20 indices)
2026-05-24 09:47:45     Loaded (local prefetch)
2026-05-24 09:47:45    Ready: Radiant28/evolai-0.4b-V1@5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5
2026-05-24 09:47:45    Downloading snx999/evolai_qw_4b@69eff663b4e9a2b5bf76dde6cdecc5dce29759d3…
2026-05-24 09:47:45 Fetching 11 files: 100%|██████████| 11/11 [00:14<00:00,  1.36s/it]
2026-05-24 09:47:45     Model 0.47B → batch=512, seq=16384
2026-05-24 09:48:00    Ready: snx999/evolai_qw_4b@69eff663b4e9a2b5bf76dde6cdecc5dce29759d3
2026-05-24 09:48:29     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:37
2026-05-24 09:48:29     Loss 4.1163 | Size ×0.51 | Think 4.1163 | ThinkGain 0 (+0.4796) | Flow
2026-05-24 09:48:29 0.0000 | KL 3.9174 | NextKL 3.8609 | SideQ 0% | Score 0.0000 (43.7s)
2026-05-24 09:48:29     Gate FAIL | Improve same SHA cur=3.9174 req<=3.8390 prev=3.9174 | Consist ok
2026-05-24 09:48:29 ema_cur=4.3438 ema_next=3.9237 ratio=0.903 max<=1.20
2026-05-24 09:48:31   Evicted cached model:
2026-05-24 09:48:31 Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd
2026-05-24 09:48:31   [7/50] UID 44 | Radiant28/evolai-0.4b-V1 @
2026-05-24 09:48:31 5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5 | hotkey 5DXm2ShZGmwG…
2026-05-24 09:48:31     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:48:31     Fetched 20 texts (20 indices)
2026-05-24 09:48:31    Downloading
2026-05-24 09:48:31 andrebarrosilva1123/evolai-f@89654c7b1e351cce36bab65fe09692eb0e109f72…
2026-05-24 09:48:35     Loaded (local prefetch)
2026-05-24 09:48:35     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:48:38   [8/50] UID 25 | snx999/evolai_qw_4b @ 69eff663b4e9a2b5bf76dde6cdecc5dce29759d3
2026-05-24 09:48:38 | hotkey 5HBJoNWv4nAi…
2026-05-24 09:48:38     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:48:38     Fetched 20 texts (20 indices)
2026-05-24 09:48:38    Ready: andrebarrosilva1123/evolai-f@89654c7b1e351cce36bab65fe09692eb0e109f72
2026-05-24 09:48:38    Downloading
2026-05-24 09:48:38 clear-blue-sky/evolai-reborn-tfm-011@beb29d65b62fe0bf12e75930e488d4ab7baa4381…
2026-05-24 09:48:41     Loaded (local prefetch)
2026-05-24 09:48:42    Ready:
2026-05-24 09:48:42 clear-blue-sky/evolai-reborn-tfm-011@beb29d65b62fe0bf12e75930e488d4ab7baa4381
2026-05-24 09:48:42     ⚠ Invalid model size (4.21B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 09:48:44   [9/50] UID 52 | andrebarrosilva1123/evolai-f @
2026-05-24 09:48:44 89654c7b1e351cce36bab65fe09692eb0e109f72 | hotkey 5HTZZEb5oxv9…
2026-05-24 09:48:44     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:48:44     Fetched 20 texts (20 indices)
2026-05-24 09:48:44    Downloading
2026-05-24 09:48:44 mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c…
2026-05-24 09:48:47     Loaded (local prefetch)
2026-05-24 09:48:48    Ready: mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c
2026-05-24 09:48:48     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:48:51   [10/50] UID 73 | clear-blue-sky/evolai-reborn-tfm-011 @
2026-05-24 09:48:51 beb29d65b62fe0bf12e75930e488d4ab7baa4381 | hotkey 5CSAM6rnGRPk…
2026-05-24 09:48:51     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:48:51     Fetched 20 texts (20 indices)
2026-05-24 09:48:51    Downloading
2026-05-24 09:48:51 mrthor102/evolai-tfm-super-003@de0150ec822c6727975169eeb4e1413ee97549e3…
2026-05-24 09:48:54     Loaded (local prefetch)
2026-05-24 09:48:54     Model 0.46B → batch=512, seq=16384
2026-05-24 09:48:55    Ready:
2026-05-24 09:48:55 mrthor102/evolai-tfm-super-003@de0150ec822c6727975169eeb4e1413ee97549e3
2026-05-24 09:49:51     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:53
2026-05-24 09:49:51     Loss 3.7803 | Size ×0.50 | Think 3.7803 | ThinkGain 0 (+0.4618) | Flow
2026-05-24 09:49:51 0.0000 | KL 1.8252 | NextKL 1.8322 | SideQ 0% | Score 0.0000 (57.2s)
2026-05-24 09:49:51     Gate FAIL | Improve FAIL cur=1.8252 req<=1.8014 prev=1.8382 | Consist ok
2026-05-24 09:49:51 ema_cur=2.3810 ema_next=1.8511 ratio=0.777 max<=1.20
2026-05-24 09:49:53   Evicted cached model:
2026-05-24 09:49:53 mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7
2026-05-24 09:49:54   [11/50] UID 33 | mihai-777/evolai-tfm-1p5b @
2026-05-24 09:49:54 594894f806fb4c014675d89aad14f1c68976d52c | hotkey 5F22JM4of6TR…
2026-05-24 09:49:54     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:49:54    Downloading evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4…
2026-05-24 09:49:54     Fetched 20 texts (20 indices)
2026-05-24 09:49:57    Ready: evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4
2026-05-24 09:49:57     Loaded (local prefetch)
2026-05-24 09:49:57     Model 0.46B → batch=512, seq=16384
2026-05-24 09:50:46     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:45
2026-05-24 09:50:46     Loss 2.4183 | Size ×0.50 | Think 2.4183 | ThinkGain 0 (+0.4516) | Flow
2026-05-24 09:50:46 0.1455 | KL 2.2735 | NextKL 2.6364 | SideQ 0% | Score 0.0000 (48.5s)
2026-05-24 09:50:46     Gate FAIL | Improve same SHA cur=2.2735 req<=2.2280 prev=2.2735 | Consist ok
2026-05-24 09:50:46 ema_cur=2.3859 ema_next=2.4258 ratio=1.017 max<=1.20
2026-05-24 09:50:48   Evicted cached model:
2026-05-24 09:50:48 Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0
2026-05-24 09:50:48   [12/50] UID 98 | mrthor102/evolai-tfm-super-003 @
2026-05-24 09:50:48 de0150ec822c6727975169eeb4e1413ee97549e3 | hotkey 5Hgy59m2Hzm1…
2026-05-24 09:50:48     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:50:48     Fetched 20 texts (20 indices)
2026-05-24 09:50:48    Downloading
2026-05-24 09:50:48 Radiant28/evolai-transformer-0.4b-b0@7a08a8009fa8b8f82d1ad0febc442a89020082d1…
2026-05-24 09:50:50     Loaded (local prefetch)
2026-05-24 09:50:50     Model 0.46B → batch=512, seq=16384
2026-05-24 09:50:55    Ready:
2026-05-24 09:50:55 Radiant28/evolai-transformer-0.4b-b0@7a08a8009fa8b8f82d1ad0febc442a89020082d1
2026-05-24 09:51:27     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 09:51:27     Loss 3.9107 | Size ×0.50 | Think 3.9107 | ThinkGain 0 (+0.4601) | Flow
2026-05-24 09:51:27 0.0000 | KL 2.1723 | NextKL 1.7818 | SideQ 0% | Score 0.0000 (37.2s)
2026-05-24 09:51:27     Gate FAIL | Improve FAIL cur=2.1723 req<=2.1628 prev=2.2070 | Consist ok
2026-05-24 09:51:27 ema_cur=1.9373 ema_next=1.9231 ratio=0.993 max<=1.20
2026-05-24 09:51:29   Evicted cached model:
2026-05-24 09:51:29 evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a
2026-05-24 09:51:30   [13/50] UID 95 | evolai/evolai_naive_kl @
2026-05-24 09:51:30 da8203b6900f14ec1b724f3dd8c6dc35576fc3e4 | hotkey 5CXwmm7R4U6o…
2026-05-24 09:51:30     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:51:30     Fetched 20 texts (20 indices)
2026-05-24 09:51:30    Downloading
2026-05-24 09:51:30 mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a…
2026-05-24 09:51:31     Loaded (local prefetch)
2026-05-24 09:51:31     Model 0.46B → batch=512, seq=16384
2026-05-24 09:51:33    Ready: mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a
2026-05-24 09:52:09     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:52:10     Loss 2.1781 | Size ×0.50 | Think 2.1781 | ThinkGain 0 (+0.4796) | Flow
2026-05-24 09:52:10 0.3219 | KL 2.0342 | NextKL 3.0063 | SideQ 0% | Score 0.0000 (38.2s)
2026-05-24 09:52:10     Gate FAIL | Improve same SHA cur=2.0342 req<=1.9935 prev=2.0342 | Consist ok
2026-05-24 09:52:10 ema_cur=2.7522 ema_next=2.7652 ratio=1.005 max<=1.20
2026-05-24 09:52:12   Evicted cached model:
2026-05-24 09:52:12 Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d
2026-05-24 09:52:12   [14/50] UID 45 | Radiant28/evolai-transformer-0.4b-b0 @
2026-05-24 09:52:12 7a08a8009fa8b8f82d1ad0febc442a89020082d1 | hotkey 5F1B3j7EyjuE…
2026-05-24 09:52:12     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:52:12     Fetched 20 texts (20 indices)
2026-05-24 09:52:12    Downloading
2026-05-24 09:52:12 clear-blue-sky/evolai-reborn-tfm-004@07f27c41bf786068786d177c950f838c9d6e8af5…
2026-05-24 09:52:14     Loaded (local prefetch)
2026-05-24 09:52:14     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:52:16    Ready:
2026-05-24 09:52:16 clear-blue-sky/evolai-reborn-tfm-004@07f27c41bf786068786d177c950f838c9d6e8af5
2026-05-24 09:52:17   [15/50] UID 38 | mihai-777/evolai-tfm-1p5b-alt @
2026-05-24 09:52:17 5ebb4a406916abe39e32823ff1f635b70e707e5a | hotkey 5FbfiXysyCtC…
2026-05-24 09:52:17     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:52:17     Fetched 20 texts (20 indices)
2026-05-24 09:52:17    Downloading
2026-05-24 09:52:17 clear-blue-sky/evolai-reborn-tfm-001@b48f1a8209c087f4cf9a50e9c65ae7b988bd805c…
2026-05-24 09:52:18     Loaded (local prefetch)
2026-05-24 09:52:18     Model 0.46B → batch=512, seq=16384
2026-05-24 09:52:20    Ready:
2026-05-24 09:52:20 clear-blue-sky/evolai-reborn-tfm-001@b48f1a8209c087f4cf9a50e9c65ae7b988bd805c
2026-05-24 09:52:55     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 09:52:55     Loss 2.9932 | Size ×0.50 | Think 2.9932 | ThinkGain 0 (+0.4533) | Flow
2026-05-24 09:52:55 0.0000 | KL 2.7254 | NextKL 2.5457 | SideQ 0% | Score 0.0000 (37.1s)
2026-05-24 09:52:55     Gate FAIL | Improve same SHA cur=2.7254 req<=2.6709 prev=2.7254 | Consist ok
2026-05-24 09:52:55 ema_cur=2.4183 ema_next=2.4454 ratio=1.011 max<=1.20
2026-05-24 09:52:57   Evicted cached model:
2026-05-24 09:52:57 clear-blue-sky/evolai-reborn-tfm-007@22d900793d1d3e4eff1eafd02c6767bd579ef7f2
2026-05-24 09:52:58   [16/50] UID 70 | clear-blue-sky/evolai-reborn-tfm-004 @
2026-05-24 09:52:58 07f27c41bf786068786d177c950f838c9d6e8af5 | hotkey 5Hdg2gHopWQK…
2026-05-24 09:52:58     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:52:58     Fetched 20 texts (20 indices)
2026-05-24 09:52:58    Downloading
2026-05-24 09:52:58 clear-blue-sky/evolai-reborn-tfm-002@0059a40a08430762a0cbea1e8349247cd66598cd…
2026-05-24 09:52:59     Loaded (local prefetch)
2026-05-24 09:53:00     Model 0.46B → batch=512, seq=16384
2026-05-24 09:53:02    Ready:
2026-05-24 09:53:02 clear-blue-sky/evolai-reborn-tfm-002@0059a40a08430762a0cbea1e8349247cd66598cd
2026-05-24 09:53:38     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 09:53:38     Loss 4.1343 | Size ×0.50 | Think 4.1343 | ThinkGain 0 (+0.4654) | Flow
2026-05-24 09:53:38 0.0000 | KL 1.9459 | NextKL 2.0369 | SideQ 0% | Score 0.0000 (38.0s)
2026-05-24 09:53:38     Gate FAIL | Improve FAIL cur=1.9459 req<=1.9197 prev=1.9589 | Consist ok
2026-05-24 09:53:38 ema_cur=1.9125 ema_next=1.9277 ratio=1.008 max<=1.20
2026-05-24 09:53:39   Evicted cached model:
2026-05-24 09:53:39 evolai/evolai_test_challenge@4f5368ca6af7b884196482aebe78f284ac8eec98
2026-05-24 09:53:40   [17/50] UID 62 | clear-blue-sky/evolai-reborn-tfm-001 @
2026-05-24 09:53:40 b48f1a8209c087f4cf9a50e9c65ae7b988bd805c | hotkey 5EjjVuNJsjqP…
2026-05-24 09:53:40     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:53:40     Fetched 20 texts (20 indices)
2026-05-24 09:53:40    Downloading
2026-05-24 09:53:40 clear-blue-sky/evolai-reborn-tfm-006@9f10e168307cb13e7a2464f800efb75adb6509cc…
2026-05-24 09:53:42     Loaded (local prefetch)
2026-05-24 09:53:42     Model 0.46B → batch=512, seq=16384
2026-05-24 09:53:44    Ready:
2026-05-24 09:53:44 clear-blue-sky/evolai-reborn-tfm-006@9f10e168307cb13e7a2464f800efb75adb6509cc
2026-05-24 09:54:18     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 09:54:19     Loss 3.6780 | Size ×0.50 | Think 3.6780 | ThinkGain 0 (+0.4577) | Flow
2026-05-24 09:54:19 0.0000 | KL 1.9395 | NextKL 2.0086 | SideQ 0% | Score 0.0000 (36.4s)
2026-05-24 09:54:19     Gate FAIL | Improve FAIL cur=1.9395 req<=1.9150 prev=1.9541 | Consist ok
2026-05-24 09:54:19 ema_cur=1.9473 ema_next=1.9383 ratio=0.995 max<=1.20
2026-05-24 09:54:20   Evicted cached model:
2026-05-24 09:54:20 Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002
2026-05-24 09:54:21   [18/50] UID 67 | clear-blue-sky/evolai-reborn-tfm-002 @
2026-05-24 09:54:21 0059a40a08430762a0cbea1e8349247cd66598cd | hotkey 5GC7k2mkTKGF…
2026-05-24 09:54:21     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:54:21     Fetched 20 texts (20 indices)
2026-05-24 09:54:21    Downloading
2026-05-24 09:54:21 andrebarrosilva1123/evolai-b@3414c0abb8793ed4af56fd5e6e536b8b0f5ac520…
2026-05-24 09:54:22     Loaded (local prefetch)
2026-05-24 09:54:23     Model 0.46B → batch=512, seq=16384
2026-05-24 09:54:27    Ready: andrebarrosilva1123/evolai-b@3414c0abb8793ed4af56fd5e6e536b8b0f5ac520
2026-05-24 09:55:01     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:55:01     Loss 3.6402 | Size ×0.50 | Think 3.6402 | ThinkGain 0 (+0.4583) | Flow
2026-05-24 09:55:01 0.4901 | KL 1.6905 | NextKL 1.8019 | SideQ 0% | Score 0.0000 (38.0s)
2026-05-24 09:55:01     Gate FAIL | Improve FAIL cur=1.6905 req<=1.6764 prev=1.7107 | Consist ok
2026-05-24 09:55:01 ema_cur=1.8732 ema_next=1.8673 ratio=0.997 max<=1.20
2026-05-24 09:55:02   Evicted cached model:
2026-05-24 09:55:02 clear-blue-sky/evolai-reborn-tfm-011@beb29d65b62fe0bf12e75930e488d4ab7baa4381
2026-05-24 09:55:03   [19/50] UID 66 | clear-blue-sky/evolai-reborn-tfm-006 @
2026-05-24 09:55:03 9f10e168307cb13e7a2464f800efb75adb6509cc | hotkey 5E4M4B5sVED5…
2026-05-24 09:55:03     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:55:03     Fetched 20 texts (20 indices)
2026-05-24 09:55:03    Downloading
2026-05-24 09:55:03 Roystar/evolai-qwen2.5-1.5b@47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1…
2026-05-24 09:55:05     Loaded (local prefetch)
2026-05-24 09:55:05     Model 0.46B → batch=512, seq=16384
2026-05-24 09:55:09    Ready: Roystar/evolai-qwen2.5-1.5b@47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1
2026-05-24 09:55:43     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 09:55:43     Loss 3.7105 | Size ×0.50 | Think 3.7105 | ThinkGain 0 (+0.4615) | Flow
2026-05-24 09:55:43 0.0000 | KL 1.7615 | NextKL 1.8549 | SideQ 0% | Score 0.0000 (37.8s)
2026-05-24 09:55:43     Gate FAIL | Improve FAIL cur=1.7615 req<=1.7307 prev=1.7661 | Consist ok
2026-05-24 09:55:43 ema_cur=1.9640 ema_next=1.9486 ratio=0.992 max<=1.20
2026-05-24 09:55:45   Evicted cached model:
2026-05-24 09:55:45 mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c
2026-05-24 09:55:45   [20/50] UID 50 | andrebarrosilva1123/evolai-b @
2026-05-24 09:55:45 3414c0abb8793ed4af56fd5e6e536b8b0f5ac520 | hotkey 5FXELcBK4WiD…
2026-05-24 09:55:45     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:55:45     Fetched 20 texts (20 indices)
2026-05-24 09:55:45    Downloading
2026-05-24 09:55:45 clear-blue-sky/evolai-reborn-tfm-008@667bd70881b10587b42ac0708b03f1e58fc404db…
2026-05-24 09:55:47     Loaded (local prefetch)
2026-05-24 09:55:48     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:55:50    Ready:
2026-05-24 09:55:50 clear-blue-sky/evolai-reborn-tfm-008@667bd70881b10587b42ac0708b03f1e58fc404db
2026-05-24 09:55:50   [21/50] UID 55 | Roystar/evolai-qwen2.5-1.5b @
2026-05-24 09:55:50 47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1 | hotkey 5DhRJtUeVA6P…
2026-05-24 09:55:50     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:55:50     Fetched 20 texts (20 indices)
2026-05-24 09:55:50    Downloading
2026-05-24 09:55:50 Radiant28/evolai-transformer-0.4b-b1@18231d7d50096d8b2744fdff1b38a7b90246ddf0…
2026-05-24 09:55:52     Loaded (local prefetch)
2026-05-24 09:55:53     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:55:55   [22/50] UID 85 | clear-blue-sky/evolai-reborn-tfm-008 @
2026-05-24 09:55:55 667bd70881b10587b42ac0708b03f1e58fc404db | hotkey 5EC5MzPj6dGb…
2026-05-24 09:55:55     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:55:55     Fetched 20 texts (20 indices)
2026-05-24 09:55:56     Loaded (local prefetch)
2026-05-24 09:55:57     Model 0.46B → batch=512, seq=16384
2026-05-24 09:55:57    Ready:
2026-05-24 09:55:57 Radiant28/evolai-transformer-0.4b-b1@18231d7d50096d8b2744fdff1b38a7b90246ddf0
2026-05-24 09:55:57    Downloading
2026-05-24 09:55:57 dexserbia/evolai-gemma2-9b@7fe66309a3847239a4da5b712477f2105e88399b…
2026-05-24 09:55:57 Fetching 6 files: 100%|██████████| 6/6 [00:29<00:00,  4.96s/it]
2026-05-24 09:56:26    Ready: dexserbia/evolai-gemma2-9b@7fe66309a3847239a4da5b712477f2105e88399b
2026-05-24 09:56:38     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:38
2026-05-24 09:56:38     Loss 3.5352 | Size ×0.50 | Think 3.5352 | ThinkGain 0 (+0.4614) | Flow
2026-05-24 09:56:38 0.0000 | KL 1.8428 | NextKL 1.8010 | SideQ 0% | Score 0.0000 (40.9s)
2026-05-24 09:56:38     Gate FAIL | Improve FAIL cur=1.8428 req<=1.8059 prev=1.8427 | Consist ok
2026-05-24 09:56:38 ema_cur=2.4632 ema_next=1.9325 ratio=0.785 max<=1.20
2026-05-24 09:56:40   Evicted cached model:
2026-05-24 09:56:40 mrthor102/evolai-tfm-super-003@de0150ec822c6727975169eeb4e1413ee97549e3
2026-05-24 09:56:40   [23/50] UID 35 | Radiant28/evolai-transformer-0.4b-b1 @
2026-05-24 09:56:40 18231d7d50096d8b2744fdff1b38a7b90246ddf0 | hotkey 5EXZBq3wQzTK…
2026-05-24 09:56:40    Downloading
2026-05-24 09:56:40 mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a…
2026-05-24 09:56:40     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:56:40     Fetched 20 texts (20 indices)
2026-05-24 09:56:42     Loaded (local prefetch)
2026-05-24 09:56:43     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:56:44    Ready: mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a
2026-05-24 09:56:45   [24/50] UID 9 | dexserbia/evolai-gemma2-9b @
2026-05-24 09:56:45 7fe66309a3847239a4da5b712477f2105e88399b | hotkey 5EbpxBkVKVNV…
2026-05-24 09:56:45     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:56:45     Fetched 20 texts (20 indices)
2026-05-24 09:56:45    Downloading
2026-05-24 09:56:45 andrebarrosilva1123/evolai-e@806394ca7f2f7c1edbe962a9471647f4d67b5e72…
2026-05-24 09:56:50     Loaded (local prefetch)
2026-05-24 09:56:51    Ready: andrebarrosilva1123/evolai-e@806394ca7f2f7c1edbe962a9471647f4d67b5e72
2026-05-24 09:56:52     ⚠ Invalid model size (9.24B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 09:56:54   [25/50] UID 75 | mihai-777/evolai-tfm-1p5b-04 @
2026-05-24 09:56:54 fb289dbfe35c595b1a586f786a19e118cc1bfc9a | hotkey 5Dnz76SAsEv8…
2026-05-24 09:56:54     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:56:54     Fetched 20 texts (20 indices)
2026-05-24 09:56:54    Downloading
2026-05-24 09:56:54 mrthor102/evolai-tfm-super-004@348a9a9756591382e8f32dbb959a3c014430c4f4…
2026-05-24 09:56:56     Loaded (local prefetch)
2026-05-24 09:56:56     Model 0.46B → batch=512, seq=16384
2026-05-24 09:56:58    Ready:
2026-05-24 09:56:58 mrthor102/evolai-tfm-super-004@348a9a9756591382e8f32dbb959a3c014430c4f4
2026-05-24 09:57:33     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 09:57:34     Loss 3.0454 | Size ×0.50 | Think 3.0454 | ThinkGain 0 (+0.4526) | Flow
2026-05-24 09:57:34 0.0000 | KL 2.7150 | NextKL 2.8338 | SideQ 0% | Score 0.0000 (37.6s)
2026-05-24 09:57:34     Gate FAIL | Improve same SHA cur=2.7150 req<=2.6607 prev=2.7150 | Consist ok
2026-05-24 09:57:34 ema_cur=2.3767 ema_next=2.4363 ratio=1.025 max<=1.20
2026-05-24 09:57:35   Evicted cached model:
2026-05-24 09:57:35 evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4
2026-05-24 09:57:36   [26/50] UID 53 | andrebarrosilva1123/evolai-e @
2026-05-24 09:57:36 806394ca7f2f7c1edbe962a9471647f4d67b5e72 | hotkey 5EFgFa93M5Vx…
2026-05-24 09:57:36     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:57:36     Fetched 20 texts (20 indices)
2026-05-24 09:57:36    Downloading galuis116/evolai-future@9058ecc436d3f8b73dc424bc80f6fcbc25ef9301…
2026-05-24 09:57:38     Loaded (local prefetch)
2026-05-24 09:57:38     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:57:40   [27/50] UID 99 | mrthor102/evolai-tfm-super-004 @
2026-05-24 09:57:40 348a9a9756591382e8f32dbb959a3c014430c4f4 | hotkey 5EnuPuwNaqmP…
2026-05-24 09:57:40     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:57:40     Fetched 20 texts (20 indices)
2026-05-24 09:57:40    Ready: galuis116/evolai-future@9058ecc436d3f8b73dc424bc80f6fcbc25ef9301
2026-05-24 09:57:40    Downloading
2026-05-24 09:57:40 Radiant28/evolai-transformer-0.4b-b2@808b61992e043ca99ff5b412a6cf61bfbb3fd793…
2026-05-24 09:57:42     Loaded (local prefetch)
2026-05-24 09:57:42     Model 0.46B → batch=512, seq=16384
2026-05-24 09:57:46    Ready:
2026-05-24 09:57:46 Radiant28/evolai-transformer-0.4b-b2@808b61992e043ca99ff5b412a6cf61bfbb3fd793
2026-05-24 09:58:21     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:58:21     Loss 3.8538 | Size ×0.50 | Think 3.8538 | ThinkGain 0 (+0.4609) | Flow
2026-05-24 09:58:21 0.0000 | KL 1.8642 | NextKL 1.8193 | SideQ 0% | Score 0.0000 (38.5s)
2026-05-24 09:58:21     Gate FAIL | Improve FAIL cur=1.8642 req<=1.8418 prev=1.8793 | Consist ok
2026-05-24 09:58:21 ema_cur=1.9584 ema_next=1.9422 ratio=0.992 max<=1.20
2026-05-24 09:58:23   Evicted cached model:
2026-05-24 09:58:23 mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a
2026-05-24 09:58:23   [28/50] UID 101 | galuis116/evolai-future @
2026-05-24 09:58:23 9058ecc436d3f8b73dc424bc80f6fcbc25ef9301 | hotkey 5DPz76uobJLT…
2026-05-24 09:58:23     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:58:23     Fetched 20 texts (20 indices)
2026-05-24 09:58:23    Downloading
2026-05-24 09:58:23 mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba…
2026-05-24 09:58:25     Loaded (local prefetch)
2026-05-24 09:58:25     Model 0.46B → batch=512, seq=16384
2026-05-24 09:58:28    Ready: mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba
2026-05-24 09:59:04     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 09:59:04     Loss 3.8481 | Size ×0.50 | Think 3.8481 | ThinkGain 0 (+0.4579) | Flow
2026-05-24 09:59:04 0.4110 | KL 1.8708 | NextKL 1.8837 | SideQ 0% | Score 0.0000 (38.6s)
2026-05-24 09:59:04     Gate FAIL | Improve FAIL cur=1.8708 req<=1.8468 prev=1.8845 | Consist ok
2026-05-24 09:59:04 ema_cur=1.8687 ema_next=1.8713 ratio=1.001 max<=1.20
2026-05-24 09:59:06   Evicted cached model:
2026-05-24 09:59:06 clear-blue-sky/evolai-reborn-tfm-004@07f27c41bf786068786d177c950f838c9d6e8af5
2026-05-24 09:59:06   [29/50] UID 37 | Radiant28/evolai-transformer-0.4b-b2 @
2026-05-24 09:59:06 808b61992e043ca99ff5b412a6cf61bfbb3fd793 | hotkey 5HjbzF3e9waA…
2026-05-24 09:59:06     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:59:06     Fetched 20 texts (20 indices)
2026-05-24 09:59:06    Downloading
2026-05-24 09:59:06 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb…
2026-05-24 09:59:08     Loaded (local prefetch)
2026-05-24 09:59:09     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 09:59:11   [30/50] UID 76 | mihai-777/evolai-tfm-1p5b-05 @
2026-05-24 09:59:11 a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba | hotkey 5GLBxPtoiB7R…
2026-05-24 09:59:11     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:59:11     Fetched 20 texts (20 indices)
2026-05-24 09:59:11    Ready:
2026-05-24 09:59:11 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb
2026-05-24 09:59:11    Downloading
2026-05-24 09:59:11 batster4/evolai-phi4-mini-dpo-v1@8217794abaf74f8e15f578a507e27b5f9b1df4c9…
2026-05-24 09:59:12     Loaded (local prefetch)
2026-05-24 09:59:13     Model 0.46B → batch=512, seq=16384
2026-05-24 09:59:26    Ready:
2026-05-24 09:59:26 batster4/evolai-phi4-mini-dpo-v1@8217794abaf74f8e15f578a507e27b5f9b1df4c9
2026-05-24 09:59:52     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 09:59:52     Loss 2.9589 | Size ×0.50 | Think 2.9589 | ThinkGain 0 (+0.4556) | Flow
2026-05-24 09:59:52 0.1389 | KL 2.1805 | NextKL 2.4715 | SideQ 0% | Score 0.0000 (38.9s)
2026-05-24 09:59:52     Gate FAIL | Improve same SHA cur=2.1805 req<=2.1369 prev=2.1805 | Consist ok
2026-05-24 09:59:52 ema_cur=2.4241 ema_next=2.4147 ratio=0.996 max<=1.20
2026-05-24 09:59:53   Evicted cached model:
2026-05-24 09:59:53 clear-blue-sky/evolai-reborn-tfm-001@b48f1a8209c087f4cf9a50e9c65ae7b988bd805c
2026-05-24 09:59:54   [31/50] UID 48 | sangerno63/evolai-transformer-v2 @
2026-05-24 09:59:54 4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb | hotkey 5ED3KNj5uEVS…
2026-05-24 09:59:54     Challenge: evolai/universal_qa(20 idx)
2026-05-24 09:59:54     Fetched 20 texts (20 indices)
2026-05-24 09:59:54    Downloading
2026-05-24 09:59:54 Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9…
2026-05-24 09:59:55     Loaded (local prefetch)
2026-05-24 09:59:56     Model 0.46B → batch=512, seq=16384
2026-05-24 09:59:58    Ready: Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9
2026-05-24 10:00:34     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:00:34     Loss 3.9549 | Size ×0.50 | Think 3.9549 | ThinkGain 0 (+0.4419) | Flow
2026-05-24 10:00:34 0.1950 | KL 2.0905 | NextKL 2.2124 | SideQ 0% | Score 0.0001 (38.2s)
2026-05-24 10:00:34     Gate FAIL | Improve same SHA cur=2.0905 req<=2.0487 prev=2.0905 | Consist ok
2026-05-24 10:00:34 ema_cur=2.1835 ema_next=2.1795 ratio=0.998 max<=1.20
2026-05-24 10:00:36   Evicted cached model:
2026-05-24 10:00:36 clear-blue-sky/evolai-reborn-tfm-002@0059a40a08430762a0cbea1e8349247cd66598cd
2026-05-24 10:00:36   [32/50] UID 59 | batster4/evolai-phi4-mini-dpo-v1 @
2026-05-24 10:00:36 8217794abaf74f8e15f578a507e27b5f9b1df4c9 | hotkey 5GCA2s6m4RRM…
2026-05-24 10:00:36     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:00:36    Downloading Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600…
2026-05-24 10:00:36     Fetched 20 texts (20 indices)
2026-05-24 10:00:39    Ready: Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600
2026-05-24 10:00:39     Loaded (local prefetch)
2026-05-24 10:00:40     ⚠ Invalid model size (3.84B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 10:00:42   [33/50] UID 93 | Phoenix9781/evolai-tf-model @
2026-05-24 10:00:42 b05038fcfdcc79fa8d8e79730074b65cd68c73f9 | hotkey 5F4R25t78FSF…
2026-05-24 10:00:42     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:00:42     Fetched 20 texts (20 indices)
2026-05-24 10:00:42    Downloading
2026-05-24 10:00:42 clear-blue-sky/evolai-reborn-tfm-009@7b9aeb06c1284c7e1c2c54a1cf770e82fd037238…
2026-05-24 10:00:44     Loaded (local prefetch)
2026-05-24 10:00:44     Model 0.46B → batch=512, seq=16384
2026-05-24 10:00:46    Ready:
2026-05-24 10:00:46 clear-blue-sky/evolai-reborn-tfm-009@7b9aeb06c1284c7e1c2c54a1cf770e82fd037238
2026-05-24 10:01:23     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:01:23     Loss 3.5716 | Size ×0.50 | Think 3.5716 | ThinkGain 0 (+0.4600) | Flow
2026-05-24 10:01:23 0.0000 | KL 2.0425 | NextKL 2.0005 | SideQ 0% | Score 0.0000 (38.3s)
2026-05-24 10:01:23     Gate FAIL | Improve same SHA cur=2.0425 req<=2.0016 prev=2.0425 | Consist ok
2026-05-24 10:01:23 ema_cur=1.9825 ema_next=1.9775 ratio=0.998 max<=1.20
2026-05-24 10:01:24   Evicted cached model:
2026-05-24 10:01:24 clear-blue-sky/evolai-reborn-tfm-006@9f10e168307cb13e7a2464f800efb75adb6509cc
2026-05-24 10:01:25   [34/50] UID 79 | Lin2es/evolai-tfm-03o @
2026-05-24 10:01:25 2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600 | hotkey 5D4eNqXRjWmX…
2026-05-24 10:01:25     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:01:25     Fetched 20 texts (20 indices)
2026-05-24 10:01:25    Downloading
2026-05-24 10:01:25 andrebarrosilva1123/evolai-d@89649e9376dace64f631711d3d270198e376702e…
2026-05-24 10:01:26     Loaded (local prefetch)
2026-05-24 10:01:26     Model 0.46B → batch=512, seq=16384
2026-05-24 10:01:31    Ready: andrebarrosilva1123/evolai-d@89649e9376dace64f631711d3d270198e376702e
2026-05-24 10:02:05     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:02:05     Loss 2.3255 | Size ×0.50 | Think 2.3255 | ThinkGain 0 (+0.4608) | Flow
2026-05-24 10:02:05 0.0000 | KL 2.2582 | NextKL 2.3064 | SideQ 0% | Score 0.0000 (38.3s)
2026-05-24 10:02:05     Gate FAIL | Improve same SHA cur=2.2582 req<=2.2130 prev=2.2582 | Consist ok
2026-05-24 10:02:05 ema_cur=2.4418 ema_next=2.4308 ratio=0.996 max<=1.20
2026-05-24 10:02:07   Evicted cached model:
2026-05-24 10:02:07 clear-blue-sky/evolai-reborn-tfm-008@667bd70881b10587b42ac0708b03f1e58fc404db
2026-05-24 10:02:07   [35/50] UID 69 | clear-blue-sky/evolai-reborn-tfm-009 @
2026-05-24 10:02:07 7b9aeb06c1284c7e1c2c54a1cf770e82fd037238 | hotkey 5ChUCf3NjrgS…
2026-05-24 10:02:07     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:02:07     Fetched 20 texts (20 indices)
2026-05-24 10:02:07    Downloading Radiant28/evolai-1p5b@e351598db6d77f85b5081768df04d37c132750f0…
2026-05-24 10:02:09     Loaded (local prefetch)
2026-05-24 10:02:09     Model 0.46B → batch=512, seq=16384
2026-05-24 10:02:14    Ready: Radiant28/evolai-1p5b@e351598db6d77f85b5081768df04d37c132750f0
2026-05-24 10:02:47     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 10:02:47     Loss 3.9550 | Size ×0.50 | Think 3.9550 | ThinkGain 0 (+0.4615) | Flow
2026-05-24 10:02:47 0.1048 | KL 2.1707 | NextKL 1.7083 | SideQ 0% | Score 0.0000 (37.5s)
2026-05-24 10:02:47     Gate FAIL | Improve FAIL cur=2.1707 req<=2.1395 prev=2.1831 | Consist ok
2026-05-24 10:02:47 ema_cur=1.9271 ema_next=1.9099 ratio=0.991 max<=1.20
2026-05-24 10:02:48   Evicted cached model:
2026-05-24 10:02:48 mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a
2026-05-24 10:02:49   [36/50] UID 51 | andrebarrosilva1123/evolai-d @
2026-05-24 10:02:49 89649e9376dace64f631711d3d270198e376702e | hotkey 5EhLiPB1GHwH…
2026-05-24 10:02:49     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:02:49     Fetched 20 texts (20 indices)
2026-05-24 10:02:49    Downloading
2026-05-24 10:02:49 andrebarrosilva1123/evolai-c@6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c…
2026-05-24 10:02:51     Loaded (local prefetch)
2026-05-24 10:02:51     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:02:54   [37/50] UID 43 | Radiant28/evolai-1p5b @
2026-05-24 10:02:54 e351598db6d77f85b5081768df04d37c132750f0 | hotkey 5HSz4knZnWHY…
2026-05-24 10:02:54     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:02:54     Fetched 20 texts (20 indices)
2026-05-24 10:02:55     Loaded (local prefetch)
2026-05-24 10:02:56     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:02:56    Ready: andrebarrosilva1123/evolai-c@6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c
2026-05-24 10:02:56    Downloading
2026-05-24 10:02:56 Jubilant/evolai-1.50b-v1@074810c41bab77c52a216e0c2f7886484e12deeb…
2026-05-24 10:02:56 Fetching 7 files: 100%|██████████| 7/7 [00:06<00:00,  1.02it/s]
2026-05-24 10:02:58   [38/50] UID 54 | andrebarrosilva1123/evolai-c @
2026-05-24 10:02:58 6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c | hotkey 5D7HPRR2QdDB…
2026-05-24 10:02:58     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:02:58     Fetched 20 texts (20 indices)
2026-05-24 10:03:00     Loaded (local prefetch)
2026-05-24 10:03:01     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:03:03   [39/50] UID 40 | Jubilant/evolai-1.50b-v1 @
2026-05-24 10:03:03 074810c41bab77c52a216e0c2f7886484e12deeb | hotkey 5Fuv43yR7tjJ…
2026-05-24 10:03:03     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:03:03     Fetched 20 texts (20 indices)
2026-05-24 10:03:04    Ready: Jubilant/evolai-1.50b-v1@074810c41bab77c52a216e0c2f7886484e12deeb
2026-05-24 10:03:04    Downloading Jubilant/evolai-1.54b@d8681d30b14cb5a597d2ff7c909998cf9d217599…
2026-05-24 10:03:14    Ready: Jubilant/evolai-1.54b@d8681d30b14cb5a597d2ff7c909998cf9d217599
2026-05-24 10:03:14    Downloading
2026-05-24 10:03:14 dreamiii0406/evolai-0p47b-v1@fea2659bdf8bd35e5382c50e4857f1ab20f20262…
2026-05-24 10:03:14     Loaded (HF download)
2026-05-24 10:03:14     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:03:14 Fetching 7 files: 100%|██████████| 7/7 [00:03<00:00,  1.96it/s]
2026-05-24 10:03:17   [40/50] UID 36 | Jubilant/evolai-1.54b @
2026-05-24 10:03:17 d8681d30b14cb5a597d2ff7c909998cf9d217599 | hotkey 5G7Co5VNfQio…
2026-05-24 10:03:17     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:03:17     Fetched 20 texts (20 indices)
2026-05-24 10:03:17    Ready: dreamiii0406/evolai-0p47b-v1@fea2659bdf8bd35e5382c50e4857f1ab20f20262
2026-05-24 10:03:17    Downloading
2026-05-24 10:03:17 mrthor102/evolai-tfm-super-002@fc09bb65a5279c806c7fdda8d5689ee8413bc87a…
2026-05-24 10:03:19     Loaded (local prefetch)
2026-05-24 10:03:20     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:03:22   [41/50] UID 80 | dreamiii0406/evolai-0p47b-v1 @
2026-05-24 10:03:22 fea2659bdf8bd35e5382c50e4857f1ab20f20262 | hotkey 5Cd2zZyMQnvp…
2026-05-24 10:03:22     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:03:22     Fetched 20 texts (20 indices)
2026-05-24 10:03:22    Ready:
2026-05-24 10:03:22 mrthor102/evolai-tfm-super-002@fc09bb65a5279c806c7fdda8d5689ee8413bc87a
2026-05-24 10:03:22    Downloading
2026-05-24 10:03:22 clear-blue-sky/evolai-reborn-tfm-003@fabfe8f714b9b58fef2aa5f4612c62483cccfb54…
2026-05-24 10:03:23     Loaded (local prefetch)
2026-05-24 10:03:23     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:03:25   [42/50] UID 97 | mrthor102/evolai-tfm-super-002 @
2026-05-24 10:03:25 fc09bb65a5279c806c7fdda8d5689ee8413bc87a | hotkey 5EcJYRJBVF5K…
2026-05-24 10:03:25     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:03:25     Fetched 20 texts (20 indices)
2026-05-24 10:03:26    Ready:
2026-05-24 10:03:26 clear-blue-sky/evolai-reborn-tfm-003@fabfe8f714b9b58fef2aa5f4612c62483cccfb54
2026-05-24 10:03:26    Downloading
2026-05-24 10:03:26 mrthor102/evolai-tfm-super-001@1f7efa4e42a9abc8cf9e4a3b13a2e4ac8c826670…
2026-05-24 10:03:26 Fetching 7 files: 100%|██████████| 7/7 [00:03<00:00,  1.82it/s]
2026-05-24 10:03:27     Loaded (local prefetch)
2026-05-24 10:03:27     Model 0.46B → batch=512, seq=16384
2026-05-24 10:03:30    Ready:
2026-05-24 10:03:30 mrthor102/evolai-tfm-super-001@1f7efa4e42a9abc8cf9e4a3b13a2e4ac8c826670
2026-05-24 10:04:04     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 10:04:05     Loss 4.0628 | Size ×0.50 | Think 4.0628 | ThinkGain 0 (+0.4626) | Flow
2026-05-24 10:04:05 0.0000 | KL 1.9608 | NextKL 1.9740 | SideQ 0% | Score 0.0000 (36.9s)
2026-05-24 10:04:05     Gate FAIL | Improve FAIL cur=1.9608 req<=1.9323 prev=1.9717 | Consist ok
2026-05-24 10:04:05 ema_cur=1.9438 ema_next=1.9457 ratio=1.001 max<=1.20
2026-05-24 10:04:06   Evicted cached model:
2026-05-24 10:04:06 mrthor102/evolai-tfm-super-004@348a9a9756591382e8f32dbb959a3c014430c4f4
2026-05-24 10:04:07   [43/50] UID 82 | clear-blue-sky/evolai-reborn-tfm-003 @
2026-05-24 10:04:07 fabfe8f714b9b58fef2aa5f4612c62483cccfb54 | hotkey 5EtDxpyqHywK…
2026-05-24 10:04:07     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:04:07     Fetched 20 texts (20 indices)
2026-05-24 10:04:07    Downloading
2026-05-24 10:04:07 clear-blue-sky/evolai-reborn-tfm-010@4c2491078d488a8604bea12f796a0845f4cf9dc1…
2026-05-24 10:04:08     Loaded (local prefetch)
2026-05-24 10:04:09     Model 0.46B → batch=512, seq=16384
2026-05-24 10:04:11    Ready:
2026-05-24 10:04:11 clear-blue-sky/evolai-reborn-tfm-010@4c2491078d488a8604bea12f796a0845f4cf9dc1
2026-05-24 10:04:48     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 10:04:48     Loss 3.7444 | Size ×0.50 | Think 3.7444 | ThinkGain 0 (+0.4599) | Flow
2026-05-24 10:04:48 0.3685 | KL 1.7614 | NextKL 1.7696 | SideQ 0% | Score 0.0000 (39.1s)
2026-05-24 10:04:48     Gate FAIL | Improve FAIL cur=1.7614 req<=1.7485 prev=1.7842 | Consist ok
2026-05-24 10:04:48 ema_cur=1.8673 ema_next=1.8802 ratio=1.007 max<=1.20
2026-05-24 10:04:49   Evicted cached model:
2026-05-24 10:04:49 galuis116/evolai-future@9058ecc436d3f8b73dc424bc80f6fcbc25ef9301
2026-05-24 10:04:50   [44/50] UID 94 | mrthor102/evolai-tfm-super-001 @
2026-05-24 10:04:50 1f7efa4e42a9abc8cf9e4a3b13a2e4ac8c826670 | hotkey 5CPXihPMoGQ2…
2026-05-24 10:04:50     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:04:50     Fetched 20 texts (20 indices)
2026-05-24 10:04:50    Downloading
2026-05-24 10:04:50 clear-blue-sky/evolai-reborn-tfm-005@d835dc6a32ce91a622b058d81de10b603cd8d770…
2026-05-24 10:04:52     Loaded (local prefetch)
2026-05-24 10:04:52     Model 0.46B → batch=512, seq=16384
2026-05-24 10:04:54    Ready:
2026-05-24 10:04:54 clear-blue-sky/evolai-reborn-tfm-005@d835dc6a32ce91a622b058d81de10b603cd8d770
2026-05-24 10:05:28     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:32
2026-05-24 10:05:28     Loss 3.8914 | Size ×0.50 | Think 3.8914 | ThinkGain 0 (+0.4590) | Flow
2026-05-24 10:05:28 0.0541 | KL 1.9852 | NextKL 2.1311 | SideQ 0% | Score 0.0000 (35.3s)
2026-05-24 10:05:28     Gate FAIL | Improve FAIL cur=1.9852 req<=1.9670 prev=2.0071 | Consist ok
2026-05-24 10:05:28 ema_cur=1.9092 ema_next=1.9438 ratio=1.018 max<=1.20
2026-05-24 10:05:29   Evicted cached model:
2026-05-24 10:05:29 mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba
2026-05-24 10:05:30   [45/50] UID 72 | clear-blue-sky/evolai-reborn-tfm-010 @
2026-05-24 10:05:30 4c2491078d488a8604bea12f796a0845f4cf9dc1 | hotkey 5H3rMcqJQcbK…
2026-05-24 10:05:30     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:05:30     Fetched 20 texts (20 indices)
2026-05-24 10:05:30    Downloading
2026-05-24 10:05:30 logosnodos/evolai-qwen-1.5b@7e121e8efe6c6b93d622e9a53972d221e763d10b…
2026-05-24 10:05:31     Loaded (local prefetch)
2026-05-24 10:05:32     Model 0.46B → batch=512, seq=16384
2026-05-24 10:06:15    Ready: logosnodos/evolai-qwen-1.5b@7e121e8efe6c6b93d622e9a53972d221e763d10b
2026-05-24 10:06:16     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:41
2026-05-24 10:06:16     Loss 3.7030 | Size ×0.50 | Think 3.7030 | ThinkGain 0 (+0.4595) | Flow
2026-05-24 10:06:16 0.0712 | KL 1.9379 | NextKL 1.8499 | SideQ 0% | Score 0.0000 (44.4s)
2026-05-24 10:06:16     Gate FAIL | Improve FAIL cur=1.9379 req<=1.9223 prev=1.9615 | Consist ok
2026-05-24 10:06:16 ema_cur=1.8923 ema_next=1.9052 ratio=1.007 max<=1.20
2026-05-24 10:06:18   Evicted cached model:
2026-05-24 10:06:18 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb
2026-05-24 10:06:19   [46/50] UID 83 | clear-blue-sky/evolai-reborn-tfm-005 @
2026-05-24 10:06:19 d835dc6a32ce91a622b058d81de10b603cd8d770 | hotkey 5G8tRiKdn5cC…
2026-05-24 10:06:19     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:06:19     Fetched 20 texts (20 indices)
2026-05-24 10:06:19    Downloading Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4…
2026-05-24 10:06:20     Loaded (local prefetch)
2026-05-24 10:06:21     Model 0.46B → batch=512, seq=16384
2026-05-24 10:06:22    Ready: Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4
2026-05-24 10:06:59     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:07:00     Loss 3.5214 | Size ×0.50 | Think 3.5214 | ThinkGain 0 (+0.4616) | Flow
2026-05-24 10:07:00 0.0000 | KL 1.8258 | NextKL 1.7304 | SideQ 0% | Score 0.0000 (38.7s)
2026-05-24 10:07:00     Gate FAIL | Improve FAIL cur=1.8258 req<=1.8135 prev=1.8505 | Consist ok
2026-05-24 10:07:00 ema_cur=2.4687 ema_next=1.9161 ratio=0.776 max<=1.20
2026-05-24 10:07:01   Evicted cached model:
2026-05-24 10:07:01 Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9
2026-05-24 10:07:02   [47/50] UID 61 | logosnodos/evolai-qwen-1.5b @
2026-05-24 10:07:02 7e121e8efe6c6b93d622e9a53972d221e763d10b | hotkey 5FNTU6ZYgKup…
2026-05-24 10:07:02     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:07:02     Fetched 20 texts (20 indices)
2026-05-24 10:07:02    Downloading
2026-05-24 10:07:02 mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678…
2026-05-24 10:07:04     Loaded (local prefetch)
2026-05-24 10:07:06    Ready: mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678
2026-05-24 10:07:08     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:07:10   [48/50] UID 92 | Lin2es/evolai-tfm-04o @
2026-05-24 10:07:10 52061d203723fdc8be09324d0c827898fcb7bdc4 | hotkey 5GefYX69KUVQ…
2026-05-24 10:07:10     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:07:10    Downloading Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59…
2026-05-24 10:07:10     Fetched 20 texts (20 indices)
2026-05-24 10:07:11     Loaded (local prefetch)
2026-05-24 10:07:11     Model 0.46B → batch=512, seq=16384
2026-05-24 10:07:13    Ready: Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59
2026-05-24 10:07:50     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:07:50     Loss 2.2828 | Size ×0.50 | Think 2.2828 | ThinkGain 0 (+0.4475) | Flow
2026-05-24 10:07:50 0.0000 | KL 2.6527 | NextKL 2.7603 | SideQ 0% | Score 0.0000 (38.3s)
2026-05-24 10:07:50     Gate FAIL | Improve same SHA cur=2.6527 req<=2.5996 prev=2.6527 | Consist ok
2026-05-24 10:07:50 ema_cur=3.0120 ema_next=2.5619 ratio=0.851 max<=1.20
2026-05-24 10:07:52   Evicted cached model:
2026-05-24 10:07:52 Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600
2026-05-24 10:07:52   [49/50] UID 42 | mihai-777/evolai-tfm-1p5b-v5 @
2026-05-24 10:07:52 bd42aeb0828dfa0126f7fc825e13b49209fec678 | hotkey 5C5WCYnsrXRz…
2026-05-24 10:07:52     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:07:52     Fetched 20 texts (20 indices)
2026-05-24 10:07:53     Loaded (local prefetch)
2026-05-24 10:07:54     Model 0.46B → batch=512, seq=16384
2026-05-24 10:08:32     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:08:32     Loss 2.7119 | Size ×0.50 | Think 2.7119 | ThinkGain 0 (+0.4549) | Flow
2026-05-24 10:08:32 0.3182 | KL 2.2778 | NextKL 2.4866 | SideQ 0% | Score 0.0000 (38.0s)
2026-05-24 10:08:32     Gate FAIL | Improve same SHA cur=2.2778 req<=2.2323 prev=2.2778 | Consist ok
2026-05-24 10:08:32 ema_cur=2.4118 ema_next=2.4296 ratio=1.007 max<=1.20
2026-05-24 10:08:34   Evicted cached model:
2026-05-24 10:08:34 clear-blue-sky/evolai-reborn-tfm-009@7b9aeb06c1284c7e1c2c54a1cf770e82fd037238
2026-05-24 10:08:34   [50/50] UID 78 | Lin2es/evolai-tfm-02o @
2026-05-24 10:08:34 fc5fc3ee4a3877b825b404dc85c9367c1f248c59 | hotkey 5FA2kgLNs36d…
2026-05-24 10:08:34     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:08:34     Fetched 20 texts (20 indices)
2026-05-24 10:08:35     Loaded (local prefetch)
2026-05-24 10:08:36     Model 0.46B → batch=512, seq=16384
2026-05-24 10:09:14     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 10:09:14     Loss 3.5280 | Size ×0.50 | Think 3.5280 | ThinkGain 0 (+0.4298) | Flow
2026-05-24 10:09:14 0.0000 | KL 3.0763 | NextKL 2.9689 | SideQ 0% | Score 0.0000 (37.9s)
2026-05-24 10:09:14     Gate FAIL | Improve same SHA cur=3.0763 req<=3.0147 prev=3.0763 | Consist ok
2026-05-24 10:09:14 ema_cur=2.8157 ema_next=2.8283 ratio=1.004 max<=1.20
2026-05-24 10:09:16   Evicted cached model:
2026-05-24 10:09:16 mrthor102/evolai-tfm-super-002@fc09bb65a5279c806c7fdda8d5689ee8413bc87a
2026-05-24 10:09:16   Cached next refs for transformer: 50 miner(s)
2026-05-24 10:09:16 
2026-05-24 10:09:16   ✓ TRANSFORMER: 30 evaluated, 23 skipped —
2026-05-24 10:09:16 epoch_22925_transformer_20260524_094240.json
2026-05-24 10:09:17   ✓ Telemetry sent (30 records)
2026-05-24 10:09:17 Evaluating MAMBA2 track…
2026-05-24 10:09:17 
2026-05-24 10:09:17   Found 15 locked mamba2 miners
2026-05-24 10:09:17    Downloading Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0…
2026-05-24 10:09:17 Pre-building current/next challenges for 15 miners…
2026-05-24 10:09:17 Fetching 7 files: 100%|██████████| 7/7 [00:02<00:00,  2.45it/s]
2026-05-24 10:09:20    Ready: Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0
2026-05-24 10:09:20    Downloading
2026-05-24 10:09:20 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c…
2026-05-24 10:09:21 Fetching 7 files: 100%|██████████| 7/7 [00:03<00:00,  2.09it/s]
2026-05-24 10:09:24    Ready:
2026-05-24 10:09:24 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c
2026-05-24 10:09:36 ✓ Ref data ready: submitted=15, cached=15
2026-05-24 10:09:36   [1/15] UID 11 | Lin2es/evolai-mb2-01v @
2026-05-24 10:09:36 a7f32e5ce7f8d307c98560e5025525f3703310c0 | hotkey 5HYuS4jrJJ56…
2026-05-24 10:09:36     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:09:36    Downloading
2026-05-24 10:09:36 Radiant28/evolai-mamba2-0.47b-v3@97f692fb0b295aa29075d3f9d592bfb4e7625b16…
2026-05-24 10:09:36     Fetched 20 texts (20 indices)
2026-05-24 10:09:38     Loaded (local prefetch)
2026-05-24 10:09:38     Model 0.48B → batch=512, seq=16384
2026-05-24 10:09:39    Ready:
2026-05-24 10:09:39 Radiant28/evolai-mamba2-0.47b-v3@97f692fb0b295aa29075d3f9d592bfb4e7625b16
2026-05-24 10:09:47     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 10:09:47     Loss 4.7112 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:09:47 0.0000 | KL 4.7112 | NextKL 4.7065 | SideQ 0% | Score 0.0000 (8.8s)
2026-05-24 10:09:47     Gate FAIL | Improve same SHA cur=4.7112 req<=4.6170 prev=4.7112 | Consist ok
2026-05-24 10:09:47 ema_cur=4.6622 ema_next=4.6736 ratio=1.002 max<=1.20
2026-05-24 10:09:49   Evicted cached model:
2026-05-24 10:09:49 clear-blue-sky/evolai-reborn-tfm-003@fabfe8f714b9b58fef2aa5f4612c62483cccfb54
2026-05-24 10:09:49   [2/15] UID 32 | mihai-777/evolai-mamba2-1p6b-alt @
2026-05-24 10:09:49 131bd3907f9816bbf184f5651ba63af66046e84c | hotkey 5GL84HKDau7C…
2026-05-24 10:09:49     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:09:49     Fetched 20 texts (20 indices)
2026-05-24 10:09:49    Downloading Lin2es/evolai-mb2-04v@9c0198682f16cc8595fec849aa37227f7160e92c…
2026-05-24 10:09:52     Loaded (local prefetch)
2026-05-24 10:09:53     Model 0.48B → batch=512, seq=16384
2026-05-24 10:09:54    Ready: Lin2es/evolai-mb2-04v@9c0198682f16cc8595fec849aa37227f7160e92c
2026-05-24 10:10:02     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:05
2026-05-24 10:10:02     Loss 4.8405 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:10:02 0.0838 | KL 4.8405 | NextKL 4.8377 | SideQ 0% | Score 0.0000 (9.0s)
2026-05-24 10:10:02     Gate FAIL | Improve same SHA cur=4.8405 req<=4.7437 prev=4.8405 | Consist ok
2026-05-24 10:10:02 ema_cur=4.8797 ema_next=4.8675 ratio=0.998 max<=1.20
2026-05-24 10:10:04   Evicted cached model:
2026-05-24 10:10:04 mrthor102/evolai-tfm-super-001@1f7efa4e42a9abc8cf9e4a3b13a2e4ac8c826670
2026-05-24 10:10:04   [3/15] UID 41 | Radiant28/evolai-mamba2-0.47b-v3 @
2026-05-24 10:10:04 97f692fb0b295aa29075d3f9d592bfb4e7625b16 | hotkey 5CP5QrWuFe93…
2026-05-24 10:10:04     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:10:04     Fetched 20 texts (20 indices)
2026-05-24 10:10:04    Downloading
2026-05-24 10:10:04 evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a…
2026-05-24 10:10:06     Loaded (local prefetch)
2026-05-24 10:10:06     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 10:10:07    Ready: evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a
2026-05-24 10:10:08   [4/15] UID 89 | Lin2es/evolai-mb2-04v @
2026-05-24 10:10:08 9c0198682f16cc8595fec849aa37227f7160e92c | hotkey 5DkZf6V3X8Za…
2026-05-24 10:10:08     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:10:08     Fetched 20 texts (20 indices)
2026-05-24 10:10:08    Downloading Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8…
2026-05-24 10:10:10     Loaded (local prefetch)
2026-05-24 10:10:11     ⚠ Vocab incompatible (model=151665 < ref=248077) — skipping
2026-05-24 10:10:11    Ready: Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8
2026-05-24 10:10:13   [5/15] UID 96 | evolai/evolai_mamba_naive_kl @
2026-05-24 10:10:13 b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a | hotkey 5HQuJVXBXGrW…
2026-05-24 10:10:13     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:10:13    Downloading
2026-05-24 10:10:13 elgin-group/evolai-mamba2-0p47b-v1@39b2f90ad08643d34503c88f5c7224fd3dabeed7…
2026-05-24 10:10:13     Fetched 20 texts (20 indices)
2026-05-24 10:10:14     Loaded (local prefetch)
2026-05-24 10:10:14     Model 0.46B → batch=512, seq=16384
2026-05-24 10:10:17    Ready:
2026-05-24 10:10:17 elgin-group/evolai-mamba2-0p47b-v1@39b2f90ad08643d34503c88f5c7224fd3dabeed7
2026-05-24 10:10:18     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 76/76 100% 0:00:01
2026-05-24 10:10:18     Loss 3.5648 | Size ×0.50 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:10:18 0.0000 | KL 3.5648 | NextKL 3.7662 | SideQ 0% | Score 0.0000 (3.9s)
2026-05-24 10:10:18     Gate FAIL | Improve same SHA cur=3.5648 req<=3.4935 prev=3.5648 | Consist ok
2026-05-24 10:10:18 ema_cur=3.8968 ema_next=3.5046 ratio=0.899 max<=1.20
2026-05-24 10:10:20   Evicted cached model:
2026-05-24 10:10:20 clear-blue-sky/evolai-reborn-tfm-010@4c2491078d488a8604bea12f796a0845f4cf9dc1
2026-05-24 10:10:20   [6/15] UID 90 | Lin2es/evolai-mb2-02v @
2026-05-24 10:10:20 c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8 | hotkey 5CtLLhrw6Lxa…
2026-05-24 10:10:20     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:10:20     Fetched 20 texts (20 indices)
2026-05-24 10:10:20    Downloading Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd…
2026-05-24 10:10:22     Loaded (local prefetch)
2026-05-24 10:10:22     Model 0.48B → batch=512, seq=16384
2026-05-24 10:10:23    Ready: Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd
2026-05-24 10:10:26     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 10:10:26     Loss 4.7207 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:10:26 0.0000 | KL 4.7207 | NextKL 4.7924 | SideQ 0% | Score 0.0000 (4.0s)
2026-05-24 10:10:26     Gate FAIL | Improve same SHA cur=4.7207 req<=4.6263 prev=4.7207 | Consist ok
2026-05-24 10:10:26 ema_cur=5.0561 ema_next=4.7175 ratio=0.933 max<=1.20
2026-05-24 10:10:28   Evicted cached model:
2026-05-24 10:10:28 clear-blue-sky/evolai-reborn-tfm-005@d835dc6a32ce91a622b058d81de10b603cd8d770
2026-05-24 10:10:28   [7/15] UID 34 | elgin-group/evolai-mamba2-0p47b-v1 @
2026-05-24 10:10:28 39b2f90ad08643d34503c88f5c7224fd3dabeed7 | hotkey 5GNJr9NfE9e9…
2026-05-24 10:10:28     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:10:28     Fetched 20 texts (20 indices)
2026-05-24 10:10:28    Downloading
2026-05-24 10:10:28 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518…
2026-05-24 10:10:30     Loaded (local prefetch)
2026-05-24 10:10:30     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 10:10:32   [8/15] UID 91 | Lin2es/evolai-mb2-03v @
2026-05-24 10:10:32 3047597c4e4b4430450ddcd633240b88d781fdbd | hotkey 5EcdUqvUBCSp…
2026-05-24 10:10:32     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:10:32     Fetched 20 texts (20 indices)
2026-05-24 10:10:32    Ready:
2026-05-24 10:10:32 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518
2026-05-24 10:10:32    Downloading
2026-05-24 10:10:32 andrebarrosilva1123/evolai-mamba2-a@55b92d373b1c219a4cfbac7034c154ddbcdc854d…
2026-05-24 10:10:33     Loaded (local prefetch)
2026-05-24 10:10:33     Model 0.48B → batch=512, seq=16384
2026-05-24 10:10:35    Ready:
2026-05-24 10:10:35 andrebarrosilva1123/evolai-mamba2-a@55b92d373b1c219a4cfbac7034c154ddbcdc854d
2026-05-24 10:10:37     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 10:10:37     Loss 4.6708 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:10:37 0.0000 | KL 4.6708 | NextKL 4.5906 | SideQ 0% | Score 0.0000 (4.0s)
2026-05-24 10:10:37     Gate FAIL | Improve same SHA cur=4.6708 req<=4.5774 prev=4.6708 | Consist ok
2026-05-24 10:10:37 ema_cur=4.6650 ema_next=4.6601 ratio=0.999 max<=1.20
2026-05-24 10:10:39   Evicted cached model:
2026-05-24 10:10:39 Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4
2026-05-24 10:10:39   [9/15] UID 30 | mihai-777/evolai-mamba2-0p47b-v3 @
2026-05-24 10:10:39 c2a96b92acf632d51a2c21da4482f77f98256518 | hotkey 5GGsbuVKDrTA…
2026-05-24 10:10:39     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:10:39     Fetched 20 texts (20 indices)
2026-05-24 10:10:39    Downloading
2026-05-24 10:10:39 andrebarrosilva1123/evolai-mamba2-c@dc37c985d66c77e3d10bf9eaf16e6dc952c62e17…
2026-05-24 10:10:41     Loaded (local prefetch)
2026-05-24 10:10:41     Model 0.48B → batch=512, seq=16384
2026-05-24 10:10:43    Ready:
2026-05-24 10:10:43 andrebarrosilva1123/evolai-mamba2-c@dc37c985d66c77e3d10bf9eaf16e6dc952c62e17
2026-05-24 10:10:46     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 10:10:46     Loss 4.5888 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:10:46 0.3514 | KL 4.5888 | NextKL 4.8142 | SideQ 0% | Score 0.0000 (4.2s)
2026-05-24 10:10:46     Gate FAIL | Improve same SHA cur=4.5888 req<=4.4970 prev=4.5888 | Consist ok
2026-05-24 10:10:46 ema_cur=4.7690 ema_next=4.7782 ratio=1.002 max<=1.20
2026-05-24 10:10:47   Evicted cached model:
2026-05-24 10:10:47 mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678
2026-05-24 10:10:48   [10/15] UID 56 | andrebarrosilva1123/evolai-mamba2-a @
2026-05-24 10:10:48 55b92d373b1c219a4cfbac7034c154ddbcdc854d | hotkey 5D1zGn2n3mzF…
2026-05-24 10:10:48     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:10:48     Fetched 20 texts (20 indices)
2026-05-24 10:10:48    Downloading
2026-05-24 10:10:48 Radiant28/evolai-mamba2-0.47b-v2@475bf7bf65af1192ed824d58816c1d83f3475983…
2026-05-24 10:10:49     Loaded (local prefetch)
2026-05-24 10:10:50     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 10:10:51   [11/15] UID 58 | andrebarrosilva1123/evolai-mamba2-c @
2026-05-24 10:10:51 dc37c985d66c77e3d10bf9eaf16e6dc952c62e17 | hotkey 5EgtSzXJbjpV…
2026-05-24 10:10:51     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:10:51     Fetched 20 texts (20 indices)
2026-05-24 10:10:51    Ready:
2026-05-24 10:10:51 Radiant28/evolai-mamba2-0.47b-v2@475bf7bf65af1192ed824d58816c1d83f3475983
2026-05-24 10:10:51    Downloading
2026-05-24 10:10:51 batster4/evolai-mamba2-v1@142f14d218be618e3161d86926085b3a9cefed55…
2026-05-24 10:10:53     Loaded (local prefetch)
2026-05-24 10:10:53     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 10:10:55   [12/15] UID 39 | Radiant28/evolai-mamba2-0.47b-v2 @
2026-05-24 10:10:55 475bf7bf65af1192ed824d58816c1d83f3475983 | hotkey 5FvTt3gVVhFT…
2026-05-24 10:10:55     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:10:55     Fetched 20 texts (20 indices)
2026-05-24 10:10:55    Ready: batster4/evolai-mamba2-v1@142f14d218be618e3161d86926085b3a9cefed55
2026-05-24 10:10:55    Downloading
2026-05-24 10:10:55 mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7…
2026-05-24 10:10:56     Loaded (local prefetch)
2026-05-24 10:10:57     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 10:10:59   [13/15] UID 60 | batster4/evolai-mamba2-v1 @
2026-05-24 10:10:59 142f14d218be618e3161d86926085b3a9cefed55 | hotkey 5Dc8EpAixcqc…
2026-05-24 10:10:59     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:10:59     Fetched 20 texts (20 indices)
2026-05-24 10:10:59    Ready: mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7
2026-05-24 10:10:59    Downloading
2026-05-24 10:10:59 andrebarrosilva1123/evolai-mamba2-b@62336a49df6d6014f779575adfd29373c228edd4…
2026-05-24 10:11:00     Loaded (local prefetch)
2026-05-24 10:11:00     ⚠ Invalid model size (0.82B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 10:11:01    Ready:
2026-05-24 10:11:01 andrebarrosilva1123/evolai-mamba2-b@62336a49df6d6014f779575adfd29373c228edd4
2026-05-24 10:11:02   [14/15] UID 31 | mihai-777/evolai-mamba2-0p47b @
2026-05-24 10:11:02 7b6564c9a46f602702c260185aa43867f321dee7 | hotkey 5CJuKKq16FkR…
2026-05-24 10:11:02     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:11:02     Fetched 20 texts (20 indices)
2026-05-24 10:11:04     Loaded (local prefetch)
2026-05-24 10:11:04     Model 0.48B → batch=512, seq=16384
2026-05-24 10:11:08     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 10:11:08     Loss 4.8005 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:11:08 0.0000 | KL 4.8005 | NextKL 4.8298 | SideQ 0% | Score 0.0000 (3.8s)
2026-05-24 10:11:08     Gate FAIL | Improve same SHA cur=4.8005 req<=4.7045 prev=4.8005 | Consist ok
2026-05-24 10:11:08 ema_cur=4.7779 ema_next=4.7787 ratio=1.000 max<=1.20
2026-05-24 10:11:10   Evicted cached model:
2026-05-24 10:11:10 Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59
2026-05-24 10:11:10   [15/15] UID 57 | andrebarrosilva1123/evolai-mamba2-b @
2026-05-24 10:11:10 62336a49df6d6014f779575adfd29373c228edd4 | hotkey 5EZx1DRvpMGK…
2026-05-24 10:11:10     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:11:10     Fetched 20 texts (20 indices)
2026-05-24 10:11:11     Loaded (local prefetch)
2026-05-24 10:11:12     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 10:11:13   Cached next refs for mamba2: 15 miner(s)
2026-05-24 10:11:13 
2026-05-24 10:11:13   ✓ MAMBA2: 7 evaluated, 14 skipped — epoch_22925_mamba2_20260524_094240.json
2026-05-24 10:11:14   ✓ Telemetry sent (7 records)
2026-05-24 10:11:14 Current Leaderboard:
2026-05-24 10:11:29 
2026-05-24 10:11:29 TRANSFORMER
2026-05-24 10:11:29 ┏━━━━━━┳━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━━━┳━━━━━━━┓
2026-05-24 10:11:29 ┃      ┃     ┃        ┃     Latest ┃           ┃       ┃     ┃         ┃       ┃
2026-05-24 10:11:29 ┃ Rank ┃ UID ┃  Score ┃       Loss ┃ ThinkGain ┃  Flow ┃ SQ% ┃      KL ┃ Evals ┃
2026-05-24 10:11:29 ┡━━━━━━╇━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━━━╇━━━━━━━┩
2026-05-24 10:11:29 │    1 │   8 │ 0.0302 │     3.8183 │  0 FAIL   │ 0.000 │  0% │  1.7714 │   310 │
2026-05-24 10:11:29 │    2 │  48 │ 0.0001 │     3.9549 │  0 FAIL   │ 0.195 │  0% │  2.0905 │   134 │
2026-05-24 10:11:29 │    3 │  82 │ 0.0000 │     3.7444 │  0 FAIL   │ 0.369 │  0% │  1.7614 │   345 │
2026-05-24 10:11:29 │    4 │  66 │ 0.0000 │     3.7105 │  0 FAIL   │ 0.000 │  0% │  1.7615 │   345 │
2026-05-24 10:11:29 │    5 │  87 │ 0.0000 │     4.0577 │  0 FAIL   │ 0.133 │  0% │  2.2495 │   147 │
2026-05-24 10:11:29 │    6 │  86 │ 0.0000 │     4.1094 │  0 FAIL   │ 0.139 │  0% │  2.3171 │   148 │
2026-05-24 10:11:29 │    7 │  73 │ 0.0000 │     3.7803 │  0 FAIL   │ 0.000 │  0% │  1.8252 │   130 │
2026-05-24 10:11:29 │    8 │  93 │ 0.0000 │     3.5716 │  0 FAIL   │ 0.000 │  0% │  2.0425 │   130 │
2026-05-24 10:11:29 │    9 │  97 │ 0.0000 │     4.0628 │  0 FAIL   │ 0.000 │  0% │  1.9608 │   260 │
2026-05-24 10:11:29 │   10 │  67 │ 0.0000 │     3.6402 │  0 FAIL   │ 0.490 │  0% │  1.6905 │   347 │
2026-05-24 10:11:29 │   11 │  70 │ 0.0000 │     4.1343 │  0 FAIL   │ 0.000 │  0% │  1.9459 │   345 │
2026-05-24 10:11:29 │   12 │  83 │ 0.0000 │     3.5214 │  0 FAIL   │ 0.000 │  0% │  1.8258 │   347 │
2026-05-24 10:11:29 │   13 │  85 │ 0.0000 │     3.5352 │  0 FAIL   │ 0.000 │  0% │  1.8428 │   334 │
2026-05-24 10:11:29 │   14 │  99 │ 0.0000 │     3.8538 │  0 FAIL   │ 0.000 │  0% │  1.8642 │   128 │
2026-05-24 10:11:29 │   15 │  72 │ 0.0000 │     3.7030 │  0 FAIL   │ 0.071 │  0% │  1.9379 │   129 │
2026-05-24 10:11:29 │   16 │  62 │ 0.0000 │     3.6780 │  0 FAIL   │ 0.000 │  0% │  1.9395 │   347 │
2026-05-24 10:11:29 │   17 │  94 │ 0.0000 │     3.8914 │  0 FAIL   │ 0.054 │  0% │  1.9852 │   260 │
2026-05-24 10:11:29 │   18 │  98 │ 0.0000 │     3.9107 │  0 FAIL   │ 0.000 │  0% │  2.1723 │   259 │
2026-05-24 10:11:29 │   19 │  69 │ 0.0000 │     3.9550 │  0 FAIL   │ 0.105 │  0% │  2.1707 │   130 │
2026-05-24 10:11:29 │   20 │   9 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   349 │
2026-05-24 10:11:29 │   21 │  25 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 10:11:29 │   22 │  33 │ 0.0000 │     2.4183 │  0 FAIL   │ 0.146 │  0% │  2.2735 │   347 │
2026-05-24 10:11:29 │   23 │  35 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:11:29 │   24 │  36 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 10:11:29 │   25 │  37 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:11:29 │   26 │  38 │ 0.0000 │     2.9932 │  0 FAIL   │ 0.000 │  0% │  2.7254 │   346 │
2026-05-24 10:11:29 │   27 │  40 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:11:29 │   28 │  42 │ 0.0000 │     2.7119 │  0 FAIL   │ 0.318 │  0% │  2.2778 │   347 │
2026-05-24 10:11:29 │   29 │  43 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:11:29 │   30 │  44 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 10:11:29 │   31 │  45 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:11:29 │   32 │  49 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 10:11:29 │   33 │  50 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 10:11:29 │   34 │  51 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   319 │
2026-05-24 10:11:29 │   35 │  52 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   320 │
2026-05-24 10:11:29 │   36 │  53 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:11:29 │   37 │  54 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   318 │
2026-05-24 10:11:29 │   38 │  55 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   350 │
2026-05-24 10:11:29 │   39 │  59 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:11:29 │   40 │  61 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:11:29 │   41 │  65 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:11:29 │   42 │  75 │ 0.0000 │     3.0454 │  0 FAIL   │ 0.000 │  0% │  2.7150 │   348 │
2026-05-24 10:11:29 │   43 │  76 │ 0.0000 │     2.9589 │  0 FAIL   │ 0.139 │  0% │  2.1805 │   346 │
2026-05-24 10:11:29 │   44 │  77 │ 0.0000 │     1.6774 │  0 FAIL   │ 0.191 │  0% │  2.1894 │   249 │
2026-05-24 10:11:29 │   45 │  78 │ 0.0000 │     3.5280 │  0 FAIL   │ 0.000 │  0% │  3.0763 │   249 │
2026-05-24 10:11:29 │   46 │  79 │ 0.0000 │     2.3255 │  0 FAIL   │ 0.000 │  0% │  2.2582 │   249 │
2026-05-24 10:11:29 │   47 │  80 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 10:11:29 │   48 │  84 │ 0.0000 │     3.7483 │  0 FAIL   │ 0.000 │  0% │  1.9477 │   331 │
2026-05-24 10:11:29 │   49 │  88 │ 0.0000 │     3.9147 │  0 FAIL   │ 0.290 │  0% │  1.9992 │   146 │
2026-05-24 10:11:29 │   50 │  92 │ 0.0000 │     2.2828 │  0 FAIL   │ 0.000 │  0% │  2.6527 │   250 │
2026-05-24 10:11:29 │   51 │  95 │ 0.0000 │     2.1781 │  0 FAIL   │ 0.322 │  0% │  2.0342 │   259 │
2026-05-24 10:11:29 │   52 │ 100 │ 0.0000 │     4.1163 │  0 FAIL   │ 0.000 │  0% │  3.9174 │   258 │
2026-05-24 10:11:29 │   53 │ 101 │ 0.0000 │     3.8481 │  0 FAIL   │ 0.411 │  0% │  1.8708 │    80 │
2026-05-24 10:11:29 └──────┴─────┴────────┴────────────┴───────────┴───────┴─────┴─────────┴───────┘
2026-05-24 10:11:29 
2026-05-24 10:11:29 MAMBA2
2026-05-24 10:11:29 ┏━━━━━━┳━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━━━┳━━━━━━━┓
2026-05-24 10:11:29 ┃      ┃     ┃        ┃     Latest ┃           ┃       ┃     ┃         ┃       ┃
2026-05-24 10:11:29 ┃ Rank ┃ UID ┃  Score ┃       Loss ┃ ThinkGain ┃  Flow ┃ SQ% ┃      KL ┃ Evals ┃
2026-05-24 10:11:29 ┡━━━━━━╇━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━━━╇━━━━━━━┩
2026-05-24 10:11:29 │    1 │  11 │ 0.0000 │     4.7112 │  0 FAIL   │ 0.000 │  0% │  4.7112 │   249 │
2026-05-24 10:11:29 │    2 │  30 │ 0.0000 │     4.5888 │  0 FAIL   │ 0.351 │  0% │  4.5888 │   344 │
2026-05-24 10:11:29 │    3 │  31 │ 0.0000 │     4.8005 │  0 FAIL   │ 0.000 │  0% │  4.8005 │   344 │
2026-05-24 10:11:29 │    4 │  32 │ 0.0000 │     4.8405 │  0 FAIL   │ 0.084 │  0% │  4.8405 │   344 │
2026-05-24 10:11:29 │    5 │  34 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 10:11:29 │    6 │  39 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 10:11:29 │    7 │  41 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 10:11:29 │    8 │  56 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 10:11:29 │    9 │  57 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 10:11:29 │   10 │  58 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 10:11:29 │   11 │  60 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   344 │
2026-05-24 10:11:29 │   12 │  63 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   271 │
2026-05-24 10:11:29 │   13 │  64 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 10:11:29 │   14 │  68 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 10:11:29 │   15 │  71 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   271 │
2026-05-24 10:11:29 │   16 │  74 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 10:11:29 │   17 │  81 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   273 │
2026-05-24 10:11:29 │   18 │  89 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   249 │
2026-05-24 10:11:29 │   19 │  90 │ 0.0000 │     4.7207 │  0 FAIL   │ 0.000 │  0% │  4.7207 │   259 │
2026-05-24 10:11:29 │   20 │  91 │ 0.0000 │     4.6708 │  0 FAIL   │ 0.000 │  0% │  4.6708 │   259 │
2026-05-24 10:11:29 │   21 │  96 │ 0.0000 │     3.5648 │  0 FAIL   │ 0.000 │  0% │  3.5648 │   259 │
2026-05-24 10:11:29 └──────┴─────┴────────┴────────────┴───────────┴───────┴─────┴─────────┴───────┘
2026-05-24 10:11:29 
2026-05-24 10:11:29 Round complete in epoch 22925 (1729s elapsed). Starting next round immediately…
2026-05-24 10:11:29 
2026-05-24 10:11:29 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2026-05-24 10:11:29 
2026-05-24 10:11:29 ━━━ Epoch #22925 (Loop #5) ━━━ block=8253268, ~18m remaining
2026-05-24 10:11:38 
2026-05-24 10:11:38   ⚠ UID 86: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:11:38 (Request ID:
2026-05-24 10:11:38 Root=1-6a12ceda-70535a7d40618e6d04cf6c00;efae14b5-41ad-4063-ad28-59bf867c62cd)
2026-05-24 10:11:38 
2026-05-24 10:11:38 Repository Not Found for url:
2026-05-24 10:11:38 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-012/revision/main.
2026-05-24 10:11:38 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:11:38 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:11:38 authenticated and your token has the required permissions.
2026-05-24 10:11:38 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:11:38 Invalid username or password.
2026-05-24 10:11:38   ⚠ UID 87: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:11:38 (Request ID:
2026-05-24 10:11:38 Root=1-6a12ceda-5b80257d4728d94a20392116;9ceeb61d-156d-42c4-9b84-b34e3b6af05f)
2026-05-24 10:11:38 
2026-05-24 10:11:38 Repository Not Found for url:
2026-05-24 10:11:38 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-013/revision/main.
2026-05-24 10:11:38 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:11:38 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:11:38 authenticated and your token has the required permissions.
2026-05-24 10:11:38 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:11:38 Invalid username or password.
2026-05-24 10:11:38   ⚠ UID 88: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:11:38 (Request ID:
2026-05-24 10:11:38 Root=1-6a12ceda-2520b5b72abb7d406e53f432;be7d73c3-dcc9-4ace-9252-0dcc0856ef0e)
2026-05-24 10:11:38 
2026-05-24 10:11:38 Repository Not Found for url:
2026-05-24 10:11:38 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-014/revision/main.
2026-05-24 10:11:38 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:11:38 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:11:38 authenticated and your token has the required permissions.
2026-05-24 10:11:38 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:11:38 Invalid username or password.
2026-05-24 10:11:39   Locked transformer revisions (50 miner(s), 3 skipped)
2026-05-24 10:11:47   ⚠ UID 63: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:11:47 (Request ID:
2026-05-24 10:11:47 Root=1-6a12cee3-23a245fd5a39de054642df16;c07c0b99-1f18-4ff9-953e-4eb066884b19)
2026-05-24 10:11:47 
2026-05-24 10:11:47 Repository Not Found for url:
2026-05-24 10:11:47 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-009/revision/main.
2026-05-24 10:11:47 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:11:47 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:11:47 authenticated and your token has the required permissions.
2026-05-24 10:11:47 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:11:47 Invalid username or password.
2026-05-24 10:11:47   ⚠ UID 64: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:11:47 (Request ID:
2026-05-24 10:11:47 Root=1-6a12cee3-78b6081910e9a57d22b20ebd;d4f980b6-7661-4a43-8141-4e995cca19eb)
2026-05-24 10:11:47 
2026-05-24 10:11:47 Repository Not Found for url:
2026-05-24 10:11:47 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-002/revision/main.
2026-05-24 10:11:47 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:11:47 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:11:47 authenticated and your token has the required permissions.
2026-05-24 10:11:47 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:11:47 Invalid username or password.
2026-05-24 10:11:47   ⚠ UID 68: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:11:47 (Request ID:
2026-05-24 10:11:47 Root=1-6a12cee3-48986a9e58e7c7a60930c7c4;c981f82c-9548-4f36-a728-60f9e1b93768)
2026-05-24 10:11:47 
2026-05-24 10:11:47 Repository Not Found for url:
2026-05-24 10:11:47 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-008/revision/main.
2026-05-24 10:11:47 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:11:47 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:11:47 authenticated and your token has the required permissions.
2026-05-24 10:11:47 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:11:47 Invalid username or password.
2026-05-24 10:11:47   ⚠ UID 71: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:11:47 (Request ID:
2026-05-24 10:11:47 Root=1-6a12cee3-1c3bcc5e6ff3d6700b0f7b4e;addb3d60-0ab2-473f-9521-4311145e7096)
2026-05-24 10:11:47 
2026-05-24 10:11:47 Repository Not Found for url:
2026-05-24 10:11:47 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-001/revision/main.
2026-05-24 10:11:47 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:11:47 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:11:47 authenticated and your token has the required permissions.
2026-05-24 10:11:47 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:11:47 Invalid username or password.
2026-05-24 10:11:47   ⚠ UID 74: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:11:47 (Request ID:
2026-05-24 10:11:47 Root=1-6a12cee3-22d84aa132bb46e82748555e;32441ff3-4309-4caa-bf2c-d75879f30b1b)
2026-05-24 10:11:47 
2026-05-24 10:11:47 Repository Not Found for url:
2026-05-24 10:11:47 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-007/revision/main.
2026-05-24 10:11:47 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:11:47 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:11:47 authenticated and your token has the required permissions.
2026-05-24 10:11:47 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:11:47 Invalid username or password.
2026-05-24 10:11:47   ⚠ UID 81: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:11:47 (Request ID:
2026-05-24 10:11:47 Root=1-6a12cee3-1a164dc61b3c039836016739;0d945c7b-03ad-4f64-8b84-2d0524951ce1)
2026-05-24 10:11:47 
2026-05-24 10:11:47 Repository Not Found for url:
2026-05-24 10:11:47 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-010/revision/main.
2026-05-24 10:11:47 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:11:47 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:11:47 authenticated and your token has the required permissions.
2026-05-24 10:11:47 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:11:47 Invalid username or password.
2026-05-24 10:11:47   Locked mamba2 revisions (15 miner(s), 6 skipped)
2026-05-24 10:12:14   Committed round seed epoch=22925 seed=7591183a...
2026-05-24 10:12:14 Evaluating TRANSFORMER track…
2026-05-24 10:12:14 
2026-05-24 10:12:14   Found 50 locked transformer miners
2026-05-24 10:12:14    Downloading
2026-05-24 10:12:14 andrebarrosilva1123/evolai-0.4b@fa913c93aa7a7449066ce870427387bd3fc7e841…
2026-05-24 10:12:14 Pre-building current/next challenges for 50 miners…
2026-05-24 10:12:14 Fetching 7 files: 100%|██████████| 7/7 [00:06<00:00,  1.02it/s]
2026-05-24 10:12:22    Ready:
2026-05-24 10:12:22 andrebarrosilva1123/evolai-0.4b@fa913c93aa7a7449066ce870427387bd3fc7e841
2026-05-24 10:12:22    Downloading Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d…
2026-05-24 10:12:22 Fetching 7 files: 100%|██████████| 7/7 [00:02<00:00,  2.36it/s]
2026-05-24 10:12:25    Ready: Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d
2026-05-24 10:13:06 ✓ Ref data ready: submitted=50, cached=50
2026-05-24 10:13:06   [1/50] UID 49 | andrebarrosilva1123/evolai-0.4b @
2026-05-24 10:13:06 fa913c93aa7a7449066ce870427387bd3fc7e841 | hotkey 5DULz3AJEisH…
2026-05-24 10:13:06     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:13:06     Fetched 20 texts (20 indices)
2026-05-24 10:13:06    Downloading
2026-05-24 10:13:06 clear-blue-sky/evolai-reborn-tfm-007@d2bced542a33ea1a24c77f4eb0068bce29e0fd66…
2026-05-24 10:13:10     Loaded (local prefetch)
2026-05-24 10:13:10     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:13:11    Ready:
2026-05-24 10:13:11 clear-blue-sky/evolai-reborn-tfm-007@d2bced542a33ea1a24c77f4eb0068bce29e0fd66
2026-05-24 10:13:13   [2/50] UID 77 | Lin2es/evolai-tfm-01o @
2026-05-24 10:13:13 d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d | hotkey 5GQydjNVEhMb…
2026-05-24 10:13:13     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:13:13    Downloading
2026-05-24 10:13:13 evolai/evolai_test_challenge@386ba71ab73e9a09c3418d80197c7ba845968d2a…
2026-05-24 10:13:13     Fetched 20 texts (20 indices)
2026-05-24 10:13:14     Loaded (local prefetch)
2026-05-24 10:13:14     Model 0.46B → batch=512, seq=16384
2026-05-24 10:13:17    Ready: evolai/evolai_test_challenge@386ba71ab73e9a09c3418d80197c7ba845968d2a
2026-05-24 10:13:32    alpha=0.005490 TAO/α  budget=0.049358
2026-05-24 10:13:48    emission scale=1.000 (active miners)
2026-05-24 10:13:48    emission scale=1.000 (active miners)
2026-05-24 10:13:48    all quality scores zero after gates — emission share redistributed to
2026-05-24 10:13:48 productive tracks
2026-05-24 10:13:49   ✓  set at 10:13:49 UTC
2026-05-24 10:14:14     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:55
2026-05-24 10:14:15     Loss 3.3423 | Size ×0.50 | Think 3.3423 | ThinkGain 0 (+0.4337) | Flow
2026-05-24 10:14:15 0.0000 | KL 2.9899 | NextKL 2.8855 | SideQ 0% | Score 0.0000 (60.1s)
2026-05-24 10:14:15     Gate FAIL | Improve same SHA cur=2.9899 req<=2.9301 prev=2.9899 | Consist ok
2026-05-24 10:14:15 ema_cur=2.5961 ema_next=2.6105 ratio=1.006 max<=1.20
2026-05-24 10:14:17   Evicted cached model:
2026-05-24 10:14:17 Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0
2026-05-24 10:14:17   [3/50] UID 84 | clear-blue-sky/evolai-reborn-tfm-007 @
2026-05-24 10:14:17 d2bced542a33ea1a24c77f4eb0068bce29e0fd66 | hotkey 5H1DaT8Dtt4N…
2026-05-24 10:14:17     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:14:17     Fetched 20 texts (20 indices)
2026-05-24 10:14:17    Downloading philk11/evolai-0.4b@822950352d63cdd145c3a7449ebfd4b51ad5ae6a…
2026-05-24 10:14:20    Ready: philk11/evolai-0.4b@822950352d63cdd145c3a7449ebfd4b51ad5ae6a
2026-05-24 10:14:20     Loaded (local prefetch)
2026-05-24 10:14:21     Model 0.46B → batch=512, seq=16384
2026-05-24 10:15:21     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:53
2026-05-24 10:15:21     Loss 3.9502 | Size ×0.50 | Think 3.9502 | ThinkGain 0 (+0.4621) | Flow
2026-05-24 10:15:21 0.0000 | KL 1.9489 | NextKL 2.0413 | SideQ 0% | Score 0.0000 (60.0s)
2026-05-24 10:15:21     Gate FAIL | Improve FAIL cur=1.9489 req<=1.8923 prev=1.9309 | Consist ok
2026-05-24 10:15:21 ema_cur=1.9475 ema_next=1.9714 ratio=1.012 max<=1.20
2026-05-24 10:15:22   Evicted cached model:
2026-05-24 10:15:22 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c
2026-05-24 10:15:24   [4/50] UID 8 | evolai/evolai_test_challenge @
2026-05-24 10:15:24 386ba71ab73e9a09c3418d80197c7ba845968d2a | hotkey 5ENhqnBoyFdz…
2026-05-24 10:15:24     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:15:24     Fetched 20 texts (20 indices)
2026-05-24 10:15:24    Downloading
2026-05-24 10:15:24 Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002…
2026-05-24 10:15:25 Fetching 7 files: 100%|██████████| 7/7 [00:04<00:00,  1.53it/s]
2026-05-24 10:15:26     Loaded (local prefetch)
2026-05-24 10:15:27     Model 0.46B → batch=512, seq=16384
2026-05-24 10:15:29    Ready: Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002
2026-05-24 10:16:23     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:53
2026-05-24 10:16:24     Loss 4.0088 | Size ×0.50 | Think 4.0088 | ThinkGain 0 (+0.4557) | Flow
2026-05-24 10:16:24 0.0000 | KL 1.6860 | NextKL 1.6091 | SideQ 0% | Score 0.0305 (56.6s)
2026-05-24 10:16:24     Gate PASS | Improve ok cur=1.6860 req<=1.8141 prev=1.8511 | Consist ok
2026-05-24 10:16:24 ema_cur=1.7577 ema_next=1.9108 ratio=1.087 max<=1.20
2026-05-24 10:16:25   Evicted cached model:
2026-05-24 10:16:25 evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a
2026-05-24 10:16:26   [5/50] UID 65 | philk11/evolai-0.4b @ 822950352d63cdd145c3a7449ebfd4b51ad5ae6a
2026-05-24 10:16:26 | hotkey 5GvHE1tHbhGv…
2026-05-24 10:16:26     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:16:26     Fetched 20 texts (20 indices)
2026-05-24 10:16:26    Downloading
2026-05-24 10:16:26 Radiant28/evolai-0.4b-V1@5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5…
2026-05-24 10:16:28     Loaded (local prefetch)
2026-05-24 10:16:28     ⚠ Invalid model size (0.60B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 10:16:31   [6/50] UID 100 | Danieli1021/evolai-qwen047-v3 @
2026-05-24 10:16:31 e01dfd3b9c54325c98bf12966bdebadace391002 | hotkey 5DMH2VrrukYd…
2026-05-24 10:16:31     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:16:31     Fetched 20 texts (20 indices)
2026-05-24 10:16:32    Ready: Radiant28/evolai-0.4b-V1@5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5
2026-05-24 10:16:32    Downloading snx999/evolai_qw_4b@69eff663b4e9a2b5bf76dde6cdecc5dce29759d3…
2026-05-24 10:16:33 Fetching 11 files: 100%|██████████| 11/11 [00:15<00:00,  1.39s/it]
2026-05-24 10:16:34     Loaded (local prefetch)
2026-05-24 10:16:34     Model 0.47B → batch=512, seq=16384
2026-05-24 10:16:49    Ready: snx999/evolai_qw_4b@69eff663b4e9a2b5bf76dde6cdecc5dce29759d3
2026-05-24 10:17:18     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:37
2026-05-24 10:17:19     Loss 3.6608 | Size ×0.51 | Think 3.6608 | ThinkGain 0 (+0.4795) | Flow
2026-05-24 10:17:19 0.0000 | KL 3.8609 | NextKL 3.9907 | SideQ 0% | Score 0.0000 (44.2s)
2026-05-24 10:17:19     Gate FAIL | Improve same SHA cur=3.8609 req<=3.7837 prev=3.8609 | Consist ok
2026-05-24 10:17:19 ema_cur=4.2955 ema_next=3.9304 ratio=0.915 max<=1.20
2026-05-24 10:17:20   Evicted cached model:
2026-05-24 10:17:20 Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8
2026-05-24 10:17:21   [7/50] UID 44 | Radiant28/evolai-0.4b-V1 @
2026-05-24 10:17:21 5e0cb9981c5c7ec29fe92d5cf1ebddcbcc002af5 | hotkey 5DXm2ShZGmwG…
2026-05-24 10:17:21     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:17:21     Fetched 20 texts (20 indices)
2026-05-24 10:17:21    Downloading
2026-05-24 10:17:21 andrebarrosilva1123/evolai-f@89654c7b1e351cce36bab65fe09692eb0e109f72…
2026-05-24 10:17:23     Loaded (local prefetch)
2026-05-24 10:17:24     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:17:26   [8/50] UID 25 | snx999/evolai_qw_4b @ 69eff663b4e9a2b5bf76dde6cdecc5dce29759d3
2026-05-24 10:17:26 | hotkey 5HBJoNWv4nAi…
2026-05-24 10:17:26     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:17:26     Fetched 20 texts (20 indices)
2026-05-24 10:17:27    Ready: andrebarrosilva1123/evolai-f@89654c7b1e351cce36bab65fe09692eb0e109f72
2026-05-24 10:17:27    Downloading
2026-05-24 10:17:27 clear-blue-sky/evolai-reborn-tfm-011@fbc1e82dc3eda483c56cd84cac3d2c6bcea94545…
2026-05-24 10:17:30     Loaded (local prefetch)
2026-05-24 10:17:32    Ready:
2026-05-24 10:17:32 clear-blue-sky/evolai-reborn-tfm-011@fbc1e82dc3eda483c56cd84cac3d2c6bcea94545
2026-05-24 10:17:32     ⚠ Invalid model size (4.21B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 10:17:34   [9/50] UID 52 | andrebarrosilva1123/evolai-f @
2026-05-24 10:17:34 89654c7b1e351cce36bab65fe09692eb0e109f72 | hotkey 5HTZZEb5oxv9…
2026-05-24 10:17:34     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:17:34     Fetched 20 texts (20 indices)
2026-05-24 10:17:34    Downloading
2026-05-24 10:17:34 mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c…
2026-05-24 10:17:37     Loaded (local prefetch)
2026-05-24 10:17:38    Ready: mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c
2026-05-24 10:17:38     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:17:41   [10/50] UID 73 | clear-blue-sky/evolai-reborn-tfm-011 @
2026-05-24 10:17:41 fbc1e82dc3eda483c56cd84cac3d2c6bcea94545 | hotkey 5CSAM6rnGRPk…
2026-05-24 10:17:41     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:17:41     Fetched 20 texts (20 indices)
2026-05-24 10:17:41    Downloading
2026-05-24 10:17:41 mrthor102/evolai-tfm-super-003@e678c342500e51445e7d4bbf52a79586c65dc493…
2026-05-24 10:17:44     Loaded (local prefetch)
2026-05-24 10:17:44     Model 0.46B → batch=512, seq=16384
2026-05-24 10:17:45    Ready:
2026-05-24 10:17:45 mrthor102/evolai-tfm-super-003@e678c342500e51445e7d4bbf52a79586c65dc493
2026-05-24 10:18:42     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:54
2026-05-24 10:18:43     Loss 3.9111 | Size ×0.50 | Think 3.9111 | ThinkGain 0 (+0.4618) | Flow
2026-05-24 10:18:43 0.0000 | KL 1.8439 | NextKL 1.9427 | SideQ 0% | Score 0.0000 (57.8s)
2026-05-24 10:18:43     Gate FAIL | Improve FAIL cur=1.8439 req<=1.7956 prev=1.8322 | Consist ok
2026-05-24 10:18:43 ema_cur=2.3273 ema_next=1.8603 ratio=0.799 max<=1.20
2026-05-24 10:18:44   Evicted cached model:
2026-05-24 10:18:44 Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd
2026-05-24 10:18:45   [11/50] UID 33 | mihai-777/evolai-tfm-1p5b @
2026-05-24 10:18:45 594894f806fb4c014675d89aad14f1c68976d52c | hotkey 5F22JM4of6TR…
2026-05-24 10:18:45     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:18:45     Fetched 20 texts (20 indices)
2026-05-24 10:18:45    Downloading evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4…
2026-05-24 10:18:48     Loaded (local prefetch)
2026-05-24 10:18:48     Model 0.46B → batch=512, seq=16384
2026-05-24 10:18:48    Ready: evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4
2026-05-24 10:19:32     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:40
2026-05-24 10:19:32     Loss 2.9179 | Size ×0.50 | Think 2.9179 | ThinkGain 0 (+0.4527) | Flow
2026-05-24 10:19:32 0.0000 | KL 2.6364 | NextKL 2.4184 | SideQ 0% | Score 0.0000 (43.8s)
2026-05-24 10:19:32     Gate FAIL | Improve same SHA cur=2.6364 req<=2.5837 prev=2.6364 | Consist ok
2026-05-24 10:19:32 ema_cur=2.4110 ema_next=2.4250 ratio=1.006 max<=1.20
2026-05-24 10:19:34   Evicted cached model:
2026-05-24 10:19:34 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518
2026-05-24 10:19:35   [12/50] UID 98 | mrthor102/evolai-tfm-super-003 @
2026-05-24 10:19:35 e678c342500e51445e7d4bbf52a79586c65dc493 | hotkey 5Hgy59m2Hzm1…
2026-05-24 10:19:35     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:19:35     Fetched 20 texts (20 indices)
2026-05-24 10:19:35    Downloading
2026-05-24 10:19:35 Radiant28/evolai-transformer-0.4b-b0@7a08a8009fa8b8f82d1ad0febc442a89020082d1…
2026-05-24 10:19:36     Loaded (local prefetch)
2026-05-24 10:19:36     Model 0.46B → batch=512, seq=16384
2026-05-24 10:19:41    Ready:
2026-05-24 10:19:41 Radiant28/evolai-transformer-0.4b-b0@7a08a8009fa8b8f82d1ad0febc442a89020082d1
2026-05-24 10:20:12     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:33
2026-05-24 10:20:12     Loss 3.8191 | Size ×0.50 | Think 3.8191 | ThinkGain 0 (+0.4610) | Flow
2026-05-24 10:20:12 0.0000 | KL 1.7783 | NextKL 1.6837 | SideQ 0% | Score 0.0000 (35.7s)
2026-05-24 10:20:12     Gate FAIL | Improve FAIL cur=1.7783 req<=1.7462 prev=1.7818 | Consist ok
2026-05-24 10:20:12 ema_cur=1.9214 ema_next=1.8992 ratio=0.988 max<=1.20
2026-05-24 10:20:13   Evicted cached model:
2026-05-24 10:20:13 mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7
2026-05-24 10:20:14   [13/50] UID 95 | evolai/evolai_naive_kl @
2026-05-24 10:20:14 da8203b6900f14ec1b724f3dd8c6dc35576fc3e4 | hotkey 5CXwmm7R4U6o…
2026-05-24 10:20:14    Downloading
2026-05-24 10:20:14 mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a…
2026-05-24 10:20:14     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:20:14     Fetched 20 texts (20 indices)
2026-05-24 10:20:16     Loaded (local prefetch)
2026-05-24 10:20:16     Model 0.46B → batch=512, seq=16384
2026-05-24 10:20:18    Ready: mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a
2026-05-24 10:20:53     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 10:20:53     Loss 2.9910 | Size ×0.50 | Think 2.9910 | ThinkGain 0 (+0.4809) | Flow
2026-05-24 10:20:53 0.2190 | KL 3.0063 | NextKL 2.8653 | SideQ 0% | Score 0.0000 (36.9s)
2026-05-24 10:20:53     Gate FAIL | Improve same SHA cur=3.0063 req<=2.9462 prev=3.0063 | Consist ok
2026-05-24 10:20:53 ema_cur=2.7777 ema_next=2.7752 ratio=0.999 max<=1.20
2026-05-24 10:20:55   Evicted cached model:
2026-05-24 10:20:55 Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d
2026-05-24 10:20:55   [14/50] UID 45 | Radiant28/evolai-transformer-0.4b-b0 @
2026-05-24 10:20:55 7a08a8009fa8b8f82d1ad0febc442a89020082d1 | hotkey 5F1B3j7EyjuE…
2026-05-24 10:20:55     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:20:55     Fetched 20 texts (20 indices)
2026-05-24 10:20:55    Downloading
2026-05-24 10:20:55 clear-blue-sky/evolai-reborn-tfm-004@1b7a20c1e3e717f6c3a6d502345af1e2a1d9c8a1…
2026-05-24 10:20:57     Loaded (local prefetch)
2026-05-24 10:20:58     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:21:00   [15/50] UID 38 | mihai-777/evolai-tfm-1p5b-alt @
2026-05-24 10:21:00 5ebb4a406916abe39e32823ff1f635b70e707e5a | hotkey 5FbfiXysyCtC…
2026-05-24 10:21:00     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:21:00     Fetched 20 texts (20 indices)
2026-05-24 10:21:00    Ready:
2026-05-24 10:21:00 clear-blue-sky/evolai-reborn-tfm-004@1b7a20c1e3e717f6c3a6d502345af1e2a1d9c8a1
2026-05-24 10:21:00    Downloading
2026-05-24 10:21:00 clear-blue-sky/evolai-reborn-tfm-001@849ce9e7095269f97519168a380e220be53a4e6b…
2026-05-24 10:21:02     Loaded (local prefetch)
2026-05-24 10:21:02     Model 0.46B → batch=512, seq=16384
2026-05-24 10:21:04    Ready:
2026-05-24 10:21:04 clear-blue-sky/evolai-reborn-tfm-001@849ce9e7095269f97519168a380e220be53a4e6b
2026-05-24 10:21:40     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 10:21:40     Loss 3.2578 | Size ×0.50 | Think 3.2578 | ThinkGain 0 (+0.4549) | Flow
2026-05-24 10:21:40 0.0000 | KL 2.5457 | NextKL 2.7758 | SideQ 0% | Score 0.0000 (37.8s)
2026-05-24 10:21:40     Gate FAIL | Improve same SHA cur=2.5457 req<=2.4948 prev=2.5457 | Consist ok
2026-05-24 10:21:40 ema_cur=2.4310 ema_next=2.4785 ratio=1.020 max<=1.20
2026-05-24 10:21:42   Evicted cached model:
2026-05-24 10:21:42 clear-blue-sky/evolai-reborn-tfm-007@d2bced542a33ea1a24c77f4eb0068bce29e0fd66
2026-05-24 10:21:42   [16/50] UID 70 | clear-blue-sky/evolai-reborn-tfm-004 @
2026-05-24 10:21:42 1b7a20c1e3e717f6c3a6d502345af1e2a1d9c8a1 | hotkey 5Hdg2gHopWQK…
2026-05-24 10:21:42     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:21:42    Downloading
2026-05-24 10:21:42 clear-blue-sky/evolai-reborn-tfm-002@788609eeef48e7bfc4d300a5a17af0141d2be4c3…
2026-05-24 10:21:42     Fetched 20 texts (20 indices)
2026-05-24 10:21:44     Loaded (local prefetch)
2026-05-24 10:21:44     Model 0.46B → batch=512, seq=16384
2026-05-24 10:21:46    Ready:
2026-05-24 10:21:46 clear-blue-sky/evolai-reborn-tfm-002@788609eeef48e7bfc4d300a5a17af0141d2be4c3
2026-05-24 10:22:21     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 10:22:21     Loss 3.5738 | Size ×0.50 | Think 3.5738 | ThinkGain 0 (+0.4636) | Flow
2026-05-24 10:22:21 0.0000 | KL 2.0589 | NextKL 2.0423 | SideQ 0% | Score 0.0000 (36.9s)
2026-05-24 10:22:21     Gate FAIL | Improve FAIL cur=2.0589 req<=1.9962 prev=2.0369 | Consist ok
2026-05-24 10:22:21 ema_cur=1.9271 ema_next=1.9391 ratio=1.006 max<=1.20
2026-05-24 10:22:23   Evicted cached model:
2026-05-24 10:22:23 evolai/evolai_test_challenge@386ba71ab73e9a09c3418d80197c7ba845968d2a
2026-05-24 10:22:23   [17/50] UID 62 | clear-blue-sky/evolai-reborn-tfm-001 @
2026-05-24 10:22:23 849ce9e7095269f97519168a380e220be53a4e6b | hotkey 5EjjVuNJsjqP…
2026-05-24 10:22:23     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:22:23     Fetched 20 texts (20 indices)
2026-05-24 10:22:23    Downloading
2026-05-24 10:22:23 clear-blue-sky/evolai-reborn-tfm-006@3abb0e95402025da8fbd282c334b989c9930a680…
2026-05-24 10:22:25     Loaded (local prefetch)
2026-05-24 10:22:25     Model 0.46B → batch=512, seq=16384
2026-05-24 10:22:27    Ready:
2026-05-24 10:22:27 clear-blue-sky/evolai-reborn-tfm-006@3abb0e95402025da8fbd282c334b989c9930a680
2026-05-24 10:23:03     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:23:03     Loss 3.8257 | Size ×0.50 | Think 3.8257 | ThinkGain 0 (+0.4582) | Flow
2026-05-24 10:23:03 0.0000 | KL 2.0294 | NextKL 1.7394 | SideQ 0% | Score 0.0000 (37.7s)
2026-05-24 10:23:03     Gate FAIL | Improve FAIL cur=2.0294 req<=1.9684 prev=2.0086 | Consist ok
2026-05-24 10:23:03 ema_cur=1.9555 ema_next=1.9184 ratio=0.981 max<=1.20
2026-05-24 10:23:05   Evicted cached model:
2026-05-24 10:23:05 Danieli1021/evolai-qwen047-v3@e01dfd3b9c54325c98bf12966bdebadace391002
2026-05-24 10:23:05   [18/50] UID 67 | clear-blue-sky/evolai-reborn-tfm-002 @
2026-05-24 10:23:05 788609eeef48e7bfc4d300a5a17af0141d2be4c3 | hotkey 5GC7k2mkTKGF…
2026-05-24 10:23:05     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:23:05     Fetched 20 texts (20 indices)
2026-05-24 10:23:05    Downloading
2026-05-24 10:23:05 andrebarrosilva1123/evolai-b@3414c0abb8793ed4af56fd5e6e536b8b0f5ac520…
2026-05-24 10:23:07     Loaded (local prefetch)
2026-05-24 10:23:07     Model 0.46B → batch=512, seq=16384
2026-05-24 10:23:12    Ready: andrebarrosilva1123/evolai-b@3414c0abb8793ed4af56fd5e6e536b8b0f5ac520
2026-05-24 10:23:44     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 10:23:44     Loss 3.6214 | Size ×0.50 | Think 3.6214 | ThinkGain 0 (+0.4593) | Flow
2026-05-24 10:23:44 0.5128 | KL 1.8223 | NextKL 1.8108 | SideQ 0% | Score 0.0000 (36.5s)
2026-05-24 10:23:44     Gate FAIL | Improve FAIL cur=1.8223 req<=1.7659 prev=1.8019 | Consist ok
2026-05-24 10:23:44 ema_cur=1.8681 ema_next=1.8617 ratio=0.997 max<=1.20
2026-05-24 10:23:45   Evicted cached model:
2026-05-24 10:23:45 clear-blue-sky/evolai-reborn-tfm-011@fbc1e82dc3eda483c56cd84cac3d2c6bcea94545
2026-05-24 10:23:46   [19/50] UID 66 | clear-blue-sky/evolai-reborn-tfm-006 @
2026-05-24 10:23:46 3abb0e95402025da8fbd282c334b989c9930a680 | hotkey 5E4M4B5sVED5…
2026-05-24 10:23:46     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:23:46     Fetched 20 texts (20 indices)
2026-05-24 10:23:46    Downloading
2026-05-24 10:23:46 Roystar/evolai-qwen2.5-1.5b@47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1…
2026-05-24 10:23:48     Loaded (local prefetch)
2026-05-24 10:23:48     Model 0.46B → batch=512, seq=16384
2026-05-24 10:23:52    Ready: Roystar/evolai-qwen2.5-1.5b@47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1
2026-05-24 10:24:25     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 10:24:26     Loss 3.5299 | Size ×0.50 | Think 3.5299 | ThinkGain 0 (+0.4618) | Flow
2026-05-24 10:24:26 0.0658 | KL 1.8533 | NextKL 1.8187 | SideQ 0% | Score 0.0000 (37.4s)
2026-05-24 10:24:26     Gate FAIL | Improve FAIL cur=1.8533 req<=1.8178 prev=1.8549 | Consist ok
2026-05-24 10:24:26 ema_cur=1.9530 ema_next=1.9356 ratio=0.991 max<=1.20
2026-05-24 10:24:27   Evicted cached model:
2026-05-24 10:24:27 mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c
2026-05-24 10:24:28   [20/50] UID 50 | andrebarrosilva1123/evolai-b @
2026-05-24 10:24:28 3414c0abb8793ed4af56fd5e6e536b8b0f5ac520 | hotkey 5FXELcBK4WiD…
2026-05-24 10:24:28     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:24:28    Downloading
2026-05-24 10:24:28 clear-blue-sky/evolai-reborn-tfm-008@6b610bf06ad90c1a56fc10b2498c124808f68fec…
2026-05-24 10:24:28     Fetched 20 texts (20 indices)
2026-05-24 10:24:30     Loaded (local prefetch)
2026-05-24 10:24:30     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:24:32   [21/50] UID 55 | Roystar/evolai-qwen2.5-1.5b @
2026-05-24 10:24:32 47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1 | hotkey 5DhRJtUeVA6P…
2026-05-24 10:24:32     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:24:32     Fetched 20 texts (20 indices)
2026-05-24 10:24:32    Ready:
2026-05-24 10:24:32 clear-blue-sky/evolai-reborn-tfm-008@6b610bf06ad90c1a56fc10b2498c124808f68fec
2026-05-24 10:24:32    Downloading
2026-05-24 10:24:32 Radiant28/evolai-transformer-0.4b-b1@18231d7d50096d8b2744fdff1b38a7b90246ddf0…
2026-05-24 10:24:34     Loaded (local prefetch)
2026-05-24 10:24:35     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:24:37   [22/50] UID 85 | clear-blue-sky/evolai-reborn-tfm-008 @
2026-05-24 10:24:37 6b610bf06ad90c1a56fc10b2498c124808f68fec | hotkey 5EC5MzPj6dGb…
2026-05-24 10:24:37     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:24:37     Fetched 20 texts (20 indices)
2026-05-24 10:24:38    Ready:
2026-05-24 10:24:38 Radiant28/evolai-transformer-0.4b-b1@18231d7d50096d8b2744fdff1b38a7b90246ddf0
2026-05-24 10:24:38    Downloading
2026-05-24 10:24:38 dexserbia/evolai-gemma2-9b@7fe66309a3847239a4da5b712477f2105e88399b…
2026-05-24 10:24:38     Loaded (local prefetch)
2026-05-24 10:24:38 Fetching 6 files: 100%|██████████| 6/6 [00:29<00:00,  4.98s/it]
2026-05-24 10:24:39     Model 0.46B → batch=512, seq=16384
2026-05-24 10:25:08    Ready: dexserbia/evolai-gemma2-9b@7fe66309a3847239a4da5b712477f2105e88399b
2026-05-24 10:25:20     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:37
2026-05-24 10:25:20     Loss 3.5537 | Size ×0.50 | Think 3.5537 | ThinkGain 0 (+0.4605) | Flow
2026-05-24 10:25:20 0.0000 | KL 1.8171 | NextKL 1.7520 | SideQ 0% | Score 0.0000 (40.9s)
2026-05-24 10:25:20     Gate FAIL | Improve FAIL cur=1.8171 req<=1.7650 prev=1.8010 | Consist ok
2026-05-24 10:25:20 ema_cur=2.3986 ema_next=1.9144 ratio=0.798 max<=1.20
2026-05-24 10:25:22   Evicted cached model:
2026-05-24 10:25:22 mrthor102/evolai-tfm-super-003@e678c342500e51445e7d4bbf52a79586c65dc493
2026-05-24 10:25:22   [23/50] UID 35 | Radiant28/evolai-transformer-0.4b-b1 @
2026-05-24 10:25:22 18231d7d50096d8b2744fdff1b38a7b90246ddf0 | hotkey 5EXZBq3wQzTK…
2026-05-24 10:25:22     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:25:22     Fetched 20 texts (20 indices)
2026-05-24 10:25:22    Downloading
2026-05-24 10:25:22 mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a…
2026-05-24 10:25:24     Loaded (local prefetch)
2026-05-24 10:25:25     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:25:27   [24/50] UID 9 | dexserbia/evolai-gemma2-9b @
2026-05-24 10:25:27 7fe66309a3847239a4da5b712477f2105e88399b | hotkey 5EbpxBkVKVNV…
2026-05-24 10:25:27     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:25:27     Fetched 20 texts (20 indices)
2026-05-24 10:25:27    Ready: mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a
2026-05-24 10:25:27    Downloading
2026-05-24 10:25:27 andrebarrosilva1123/evolai-e@806394ca7f2f7c1edbe962a9471647f4d67b5e72…
2026-05-24 10:25:32     Loaded (local prefetch)
2026-05-24 10:25:34    Ready: andrebarrosilva1123/evolai-e@806394ca7f2f7c1edbe962a9471647f4d67b5e72
2026-05-24 10:25:34     ⚠ Invalid model size (9.24B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 10:25:36   [25/50] UID 75 | mihai-777/evolai-tfm-1p5b-04 @
2026-05-24 10:25:36 fb289dbfe35c595b1a586f786a19e118cc1bfc9a | hotkey 5Dnz76SAsEv8…
2026-05-24 10:25:36     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:25:36     Fetched 20 texts (20 indices)
2026-05-24 10:25:36    Downloading
2026-05-24 10:25:36 mrthor102/evolai-tfm-super-004@ad4faa7a02f71163aea95b31c05593e16888f294…
2026-05-24 10:25:37     Loaded (local prefetch)
2026-05-24 10:25:38     Model 0.46B → batch=512, seq=16384
2026-05-24 10:25:41    Ready:
2026-05-24 10:25:41 mrthor102/evolai-tfm-super-004@ad4faa7a02f71163aea95b31c05593e16888f294
2026-05-24 10:26:16     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:26:16     Loss 3.3909 | Size ×0.50 | Think 3.3909 | ThinkGain 0 (+0.4550) | Flow
2026-05-24 10:26:16 0.0000 | KL 2.8338 | NextKL 2.4272 | SideQ 0% | Score 0.0000 (38.2s)
2026-05-24 10:26:16     Gate FAIL | Improve same SHA cur=2.8338 req<=2.7771 prev=2.8338 | Consist ok
2026-05-24 10:26:16 ema_cur=2.4224 ema_next=2.4354 ratio=1.005 max<=1.20
2026-05-24 10:26:18   Evicted cached model:
2026-05-24 10:26:18 evolai/evolai_naive_kl@da8203b6900f14ec1b724f3dd8c6dc35576fc3e4
2026-05-24 10:26:18   [26/50] UID 53 | andrebarrosilva1123/evolai-e @
2026-05-24 10:26:18 806394ca7f2f7c1edbe962a9471647f4d67b5e72 | hotkey 5EFgFa93M5Vx…
2026-05-24 10:26:18     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:26:18    Downloading galuis116/evolai-future@7f5fd96012be5ad46b4bb52d24f6f07211f16492…
2026-05-24 10:26:18     Fetched 20 texts (20 indices)
2026-05-24 10:26:20     Loaded (local prefetch)
2026-05-24 10:26:20     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:26:22    Ready: galuis116/evolai-future@7f5fd96012be5ad46b4bb52d24f6f07211f16492
2026-05-24 10:26:23   [27/50] UID 99 | mrthor102/evolai-tfm-super-004 @
2026-05-24 10:26:23 ad4faa7a02f71163aea95b31c05593e16888f294 | hotkey 5EnuPuwNaqmP…
2026-05-24 10:26:23     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:26:23     Fetched 20 texts (20 indices)
2026-05-24 10:26:23    Downloading
2026-05-24 10:26:23 Radiant28/evolai-transformer-0.4b-b2@808b61992e043ca99ff5b412a6cf61bfbb3fd793…
2026-05-24 10:26:24     Loaded (local prefetch)
2026-05-24 10:26:24     Model 0.46B → batch=512, seq=16384
2026-05-24 10:26:29    Ready:
2026-05-24 10:26:29 Radiant28/evolai-transformer-0.4b-b2@808b61992e043ca99ff5b412a6cf61bfbb3fd793
2026-05-24 10:27:02     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 10:27:02     Loss 3.7980 | Size ×0.50 | Think 3.7980 | ThinkGain 0 (+0.4629) | Flow
2026-05-24 10:27:02 0.0000 | KL 1.8333 | NextKL 2.0386 | SideQ 0% | Score 0.0000 (37.4s)
2026-05-24 10:27:02     Gate FAIL | Improve FAIL cur=1.8333 req<=1.7830 prev=1.8193 | Consist ok
2026-05-24 10:27:02 ema_cur=1.9459 ema_next=1.9518 ratio=1.003 max<=1.20
2026-05-24 10:27:04   Evicted cached model:
2026-05-24 10:27:04 mihai-777/evolai-tfm-1p5b-alt@5ebb4a406916abe39e32823ff1f635b70e707e5a
2026-05-24 10:27:04   [28/50] UID 101 | galuis116/evolai-future @
2026-05-24 10:27:04 7f5fd96012be5ad46b4bb52d24f6f07211f16492 | hotkey 5DPz76uobJLT…
2026-05-24 10:27:04     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:27:04     Fetched 20 texts (20 indices)
2026-05-24 10:27:04    Downloading
2026-05-24 10:27:04 mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba…
2026-05-24 10:27:06     Loaded (local prefetch)
2026-05-24 10:27:06     Model 0.46B → batch=512, seq=16384
2026-05-24 10:27:09    Ready: mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba
2026-05-24 10:27:41     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:32
2026-05-24 10:27:41     Loss 3.6152 | Size ×0.50 | Think 3.6152 | ThinkGain 0 (+0.4591) | Flow
2026-05-24 10:27:41 0.3563 | KL 1.9061 | NextKL 1.7434 | SideQ 0% | Score 0.0000 (34.9s)
2026-05-24 10:27:41     Gate FAIL | Improve FAIL cur=1.9061 req<=1.8460 prev=1.8837 | Consist ok
2026-05-24 10:27:41 ema_cur=1.8725 ema_next=1.8585 ratio=0.993 max<=1.20
2026-05-24 10:27:42   Evicted cached model:
2026-05-24 10:27:42 clear-blue-sky/evolai-reborn-tfm-004@1b7a20c1e3e717f6c3a6d502345af1e2a1d9c8a1
2026-05-24 10:27:43   [29/50] UID 37 | Radiant28/evolai-transformer-0.4b-b2 @
2026-05-24 10:27:43 808b61992e043ca99ff5b412a6cf61bfbb3fd793 | hotkey 5HjbzF3e9waA…
2026-05-24 10:27:43     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:27:43     Fetched 20 texts (20 indices)
2026-05-24 10:27:43    Downloading
2026-05-24 10:27:43 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb…
2026-05-24 10:27:45     Loaded (local prefetch)
2026-05-24 10:27:45     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:27:48   [30/50] UID 76 | mihai-777/evolai-tfm-1p5b-05 @
2026-05-24 10:27:48 a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba | hotkey 5GLBxPtoiB7R…
2026-05-24 10:27:48     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:27:48     Fetched 20 texts (20 indices)
2026-05-24 10:27:48    Ready:
2026-05-24 10:27:48 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb
2026-05-24 10:27:48    Downloading
2026-05-24 10:27:48 batster4/evolai-phi4-mini-dpo-v1@8217794abaf74f8e15f578a507e27b5f9b1df4c9…
2026-05-24 10:27:49     Loaded (local prefetch)
2026-05-24 10:27:49     Model 0.46B → batch=512, seq=16384
2026-05-24 10:28:02    Ready:
2026-05-24 10:28:02 batster4/evolai-phi4-mini-dpo-v1@8217794abaf74f8e15f578a507e27b5f9b1df4c9
2026-05-24 10:28:28     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:28:28     Loss 2.4060 | Size ×0.50 | Think 2.4060 | ThinkGain 0 (+0.4558) | Flow
2026-05-24 10:28:28 0.1099 | KL 2.4715 | NextKL 1.8911 | SideQ 0% | Score 0.0000 (38.7s)
2026-05-24 10:28:28     Gate FAIL | Improve same SHA cur=2.4715 req<=2.4221 prev=2.4715 | Consist ok
2026-05-24 10:28:28 ema_cur=2.4288 ema_next=2.3623 ratio=0.973 max<=1.20
2026-05-24 10:28:30   Evicted cached model:
2026-05-24 10:28:30 clear-blue-sky/evolai-reborn-tfm-001@849ce9e7095269f97519168a380e220be53a4e6b
2026-05-24 10:28:30   [31/50] UID 48 | sangerno63/evolai-transformer-v2 @
2026-05-24 10:28:30 4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb | hotkey 5ED3KNj5uEVS…
2026-05-24 10:28:30     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:28:30     Fetched 20 texts (20 indices)
2026-05-24 10:28:30    Downloading
2026-05-24 10:28:30 Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9…
2026-05-24 10:28:32     Loaded (local prefetch)
2026-05-24 10:28:32     Model 0.46B → batch=512, seq=16384
2026-05-24 10:28:35    Ready: Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9
2026-05-24 10:29:11     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:29:11     Loss 4.0362 | Size ×0.50 | Think 4.0362 | ThinkGain 0 (+0.4436) | Flow
2026-05-24 10:29:11 0.1587 | KL 2.2124 | NextKL 2.0361 | SideQ 0% | Score 0.0001 (38.3s)
2026-05-24 10:29:11     Gate FAIL | Improve same SHA cur=2.2124 req<=2.1681 prev=2.2124 | Consist ok
2026-05-24 10:29:11 ema_cur=2.1864 ema_next=2.1652 ratio=0.990 max<=1.20
2026-05-24 10:29:12   Evicted cached model:
2026-05-24 10:29:12 clear-blue-sky/evolai-reborn-tfm-002@788609eeef48e7bfc4d300a5a17af0141d2be4c3
2026-05-24 10:29:13   [32/50] UID 59 | batster4/evolai-phi4-mini-dpo-v1 @
2026-05-24 10:29:13 8217794abaf74f8e15f578a507e27b5f9b1df4c9 | hotkey 5GCA2s6m4RRM…
2026-05-24 10:29:13     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:29:13     Fetched 20 texts (20 indices)
2026-05-24 10:29:13    Downloading Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600…
2026-05-24 10:29:16     Loaded (local prefetch)
2026-05-24 10:29:16    Ready: Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600
2026-05-24 10:29:17     ⚠ Invalid model size (3.84B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 10:29:19   [33/50] UID 93 | Phoenix9781/evolai-tf-model @
2026-05-24 10:29:19 b05038fcfdcc79fa8d8e79730074b65cd68c73f9 | hotkey 5F4R25t78FSF…
2026-05-24 10:29:19     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:29:19     Fetched 20 texts (20 indices)
2026-05-24 10:29:19    Downloading
2026-05-24 10:29:19 clear-blue-sky/evolai-reborn-tfm-009@461d465d0b0eae7c262990b9a8e3aa112f199ce2…
2026-05-24 10:29:20     Loaded (local prefetch)
2026-05-24 10:29:20     Model 0.46B → batch=512, seq=16384
2026-05-24 10:29:22    Ready:
2026-05-24 10:29:22 clear-blue-sky/evolai-reborn-tfm-009@461d465d0b0eae7c262990b9a8e3aa112f199ce2
2026-05-24 10:30:02     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:38
2026-05-24 10:30:02     Loss 3.8161 | Size ×0.50 | Think 3.8161 | ThinkGain 0 (+0.4600) | Flow
2026-05-24 10:30:02 0.0000 | KL 2.0005 | NextKL 1.8798 | SideQ 0% | Score 0.0000 (41.3s)
2026-05-24 10:30:02     Gate FAIL | Improve same SHA cur=2.0005 req<=1.9605 prev=2.0005 | Consist ok
2026-05-24 10:30:02 ema_cur=1.9843 ema_next=1.9678 ratio=0.992 max<=1.20
2026-05-24 10:30:04   Evicted cached model:
2026-05-24 10:30:04 clear-blue-sky/evolai-reborn-tfm-006@3abb0e95402025da8fbd282c334b989c9930a680
2026-05-24 10:30:04   [34/50] UID 79 | Lin2es/evolai-tfm-03o @
2026-05-24 10:30:04 2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600 | hotkey 5D4eNqXRjWmX…
2026-05-24 10:30:04     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:30:04     Fetched 20 texts (20 indices)
2026-05-24 10:30:04    Downloading
2026-05-24 10:30:04 andrebarrosilva1123/evolai-d@89649e9376dace64f631711d3d270198e376702e…
2026-05-24 10:30:05     Loaded (local prefetch)
2026-05-24 10:30:06     Model 0.46B → batch=512, seq=16384
2026-05-24 10:30:11    Ready: andrebarrosilva1123/evolai-d@89649e9376dace64f631711d3d270198e376702e
2026-05-24 10:30:43     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 10:30:43     Loss 1.9053 | Size ×0.50 | Think 1.9053 | ThinkGain 0 (+0.4609) | Flow
2026-05-24 10:30:43 0.0314 | KL 2.3064 | NextKL 2.4695 | SideQ 0% | Score 0.0000 (37.1s)
2026-05-24 10:30:43     Gate FAIL | Improve same SHA cur=2.3064 req<=2.2603 prev=2.3064 | Consist ok
2026-05-24 10:30:43 ema_cur=2.4282 ema_next=2.4347 ratio=1.003 max<=1.20
2026-05-24 10:30:44   Evicted cached model:
2026-05-24 10:30:44 clear-blue-sky/evolai-reborn-tfm-008@6b610bf06ad90c1a56fc10b2498c124808f68fec
2026-05-24 10:30:45   [35/50] UID 69 | clear-blue-sky/evolai-reborn-tfm-009 @
2026-05-24 10:30:45 461d465d0b0eae7c262990b9a8e3aa112f199ce2 | hotkey 5ChUCf3NjrgS…
2026-05-24 10:30:45     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:30:45    Downloading Radiant28/evolai-1p5b@e351598db6d77f85b5081768df04d37c132750f0…
2026-05-24 10:30:45     Fetched 20 texts (20 indices)
2026-05-24 10:30:46     Loaded (local prefetch)
2026-05-24 10:30:47     Model 0.46B → batch=512, seq=16384
2026-05-24 10:30:51    Ready: Radiant28/evolai-1p5b@e351598db6d77f85b5081768df04d37c132750f0
2026-05-24 10:31:25     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:31:25     Loss 3.4951 | Size ×0.50 | Think 3.4951 | ThinkGain 0 (+0.4611) | Flow
2026-05-24 10:31:25 0.2244 | KL 1.7200 | NextKL 1.8755 | SideQ 0% | Score 0.0000 (38.5s)
2026-05-24 10:31:25     Gate FAIL | Improve FAIL cur=1.7200 req<=1.6742 prev=1.7083 | Consist ok
2026-05-24 10:31:25 ema_cur=1.9064 ema_next=1.9065 ratio=1.000 max<=1.20
2026-05-24 10:31:27   Evicted cached model:
2026-05-24 10:31:27 mihai-777/evolai-tfm-1p5b-04@fb289dbfe35c595b1a586f786a19e118cc1bfc9a
2026-05-24 10:31:27   [36/50] UID 51 | andrebarrosilva1123/evolai-d @
2026-05-24 10:31:27 89649e9376dace64f631711d3d270198e376702e | hotkey 5EhLiPB1GHwH…
2026-05-24 10:31:27     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:31:27     Fetched 20 texts (20 indices)
2026-05-24 10:31:27    Downloading
2026-05-24 10:31:27 andrebarrosilva1123/evolai-c@6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c…
2026-05-24 10:31:29     Loaded (local prefetch)
2026-05-24 10:31:30     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:31:32   [37/50] UID 43 | Radiant28/evolai-1p5b @
2026-05-24 10:31:32 e351598db6d77f85b5081768df04d37c132750f0 | hotkey 5HSz4knZnWHY…
2026-05-24 10:31:32     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:31:32     Fetched 20 texts (20 indices)
2026-05-24 10:31:34    Ready: andrebarrosilva1123/evolai-c@6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c
2026-05-24 10:31:34    Downloading
2026-05-24 10:31:34 Jubilant/evolai-1.50b-v1@074810c41bab77c52a216e0c2f7886484e12deeb…
2026-05-24 10:31:34     Loaded (local prefetch)
2026-05-24 10:31:34 Fetching 7 files: 100%|██████████| 7/7 [00:06<00:00,  1.11it/s]
2026-05-24 10:31:35     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:31:37   [38/50] UID 54 | andrebarrosilva1123/evolai-c @
2026-05-24 10:31:37 6fc3d7f7c514cf3d5e4fc44dd8ef6b4ef883827c | hotkey 5D7HPRR2QdDB…
2026-05-24 10:31:37     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:31:37     Fetched 20 texts (20 indices)
2026-05-24 10:31:39     Loaded (local prefetch)
2026-05-24 10:31:40     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:31:41    Ready: Jubilant/evolai-1.50b-v1@074810c41bab77c52a216e0c2f7886484e12deeb
2026-05-24 10:31:41    Downloading Jubilant/evolai-1.54b@d8681d30b14cb5a597d2ff7c909998cf9d217599…
2026-05-24 10:31:42   [39/50] UID 40 | Jubilant/evolai-1.50b-v1 @
2026-05-24 10:31:42 074810c41bab77c52a216e0c2f7886484e12deeb | hotkey 5Fuv43yR7tjJ…
2026-05-24 10:31:42     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:31:42     Fetched 20 texts (20 indices)
2026-05-24 10:31:42 Fetching 7 files: 100%|██████████| 7/7 [00:05<00:00,  1.20it/s]
2026-05-24 10:31:43     Loaded (local prefetch)
2026-05-24 10:31:44     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:31:46   [40/50] UID 36 | Jubilant/evolai-1.54b @
2026-05-24 10:31:46 d8681d30b14cb5a597d2ff7c909998cf9d217599 | hotkey 5G7Co5VNfQio…
2026-05-24 10:31:46     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:31:46     Fetched 20 texts (20 indices)
2026-05-24 10:31:47    Ready: Jubilant/evolai-1.54b@d8681d30b14cb5a597d2ff7c909998cf9d217599
2026-05-24 10:31:47    Downloading
2026-05-24 10:31:47 dreamiii0406/evolai-0p47b-v1@fea2659bdf8bd35e5382c50e4857f1ab20f20262…
2026-05-24 10:31:52    Ready: dreamiii0406/evolai-0p47b-v1@fea2659bdf8bd35e5382c50e4857f1ab20f20262
2026-05-24 10:31:52    Downloading
2026-05-24 10:31:52 mrthor102/evolai-tfm-super-002@00a41f63a194a32daf3fcc2d6d130cbf8260880e…
2026-05-24 10:31:55     Loaded (HF download)
2026-05-24 10:31:56     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:31:57    Ready:
2026-05-24 10:31:57 mrthor102/evolai-tfm-super-002@00a41f63a194a32daf3fcc2d6d130cbf8260880e
2026-05-24 10:31:58   [41/50] UID 80 | dreamiii0406/evolai-0p47b-v1 @
2026-05-24 10:31:58 fea2659bdf8bd35e5382c50e4857f1ab20f20262 | hotkey 5Cd2zZyMQnvp…
2026-05-24 10:31:59     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:31:59    Downloading
2026-05-24 10:31:59 clear-blue-sky/evolai-reborn-tfm-003@efc7fcf7302b03d8ad811f87aceb8095dd43ddc1…
2026-05-24 10:31:59     Fetched 20 texts (20 indices)
2026-05-24 10:32:00     Loaded (local prefetch)
2026-05-24 10:32:00     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:32:02   [42/50] UID 97 | mrthor102/evolai-tfm-super-002 @
2026-05-24 10:32:02 00a41f63a194a32daf3fcc2d6d130cbf8260880e | hotkey 5EcJYRJBVF5K…
2026-05-24 10:32:02     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:32:02     Fetched 20 texts (20 indices)
2026-05-24 10:32:03    Ready:
2026-05-24 10:32:03 clear-blue-sky/evolai-reborn-tfm-003@efc7fcf7302b03d8ad811f87aceb8095dd43ddc1
2026-05-24 10:32:03    Downloading
2026-05-24 10:32:03 mrthor102/evolai-tfm-super-001@f612e4215b95fc309311d8b27cfba516801d6000…
2026-05-24 10:32:04     Loaded (local prefetch)
2026-05-24 10:32:04     Model 0.46B → batch=512, seq=16384
2026-05-24 10:32:07    Ready:
2026-05-24 10:32:07 mrthor102/evolai-tfm-super-001@f612e4215b95fc309311d8b27cfba516801d6000
2026-05-24 10:32:42     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:34
2026-05-24 10:32:42     Loss 3.8636 | Size ×0.50 | Think 3.8636 | ThinkGain 0 (+0.4639) | Flow
2026-05-24 10:32:42 0.0000 | KL 1.9914 | NextKL 1.7540 | SideQ 0% | Score 0.0000 (37.6s)
2026-05-24 10:32:42     Gate FAIL | Improve FAIL cur=1.9914 req<=1.9345 prev=1.9740 | Consist ok
2026-05-24 10:32:42 ema_cur=1.9485 ema_next=1.9266 ratio=0.989 max<=1.20
2026-05-24 10:32:44   Evicted cached model:
2026-05-24 10:32:44 mrthor102/evolai-tfm-super-004@ad4faa7a02f71163aea95b31c05593e16888f294
2026-05-24 10:32:44   [43/50] UID 82 | clear-blue-sky/evolai-reborn-tfm-003 @
2026-05-24 10:32:44 efc7fcf7302b03d8ad811f87aceb8095dd43ddc1 | hotkey 5EtDxpyqHywK…
2026-05-24 10:32:44     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:32:44     Fetched 20 texts (20 indices)
2026-05-24 10:32:44    Downloading
2026-05-24 10:32:44 clear-blue-sky/evolai-reborn-tfm-010@1533efda6c349e0b8dcc31b24b2ca15670c5da45…
2026-05-24 10:32:46     Loaded (local prefetch)
2026-05-24 10:32:46     Model 0.46B → batch=512, seq=16384
2026-05-24 10:32:48    Ready:
2026-05-24 10:32:48 clear-blue-sky/evolai-reborn-tfm-010@1533efda6c349e0b8dcc31b24b2ca15670c5da45
2026-05-24 10:33:21     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:32
2026-05-24 10:33:22     Loss 3.9337 | Size ×0.50 | Think 3.9337 | ThinkGain 0 (+0.4610) | Flow
2026-05-24 10:33:22 0.4250 | KL 1.7755 | NextKL 2.1219 | SideQ 0% | Score 0.0000 (35.2s)
2026-05-24 10:33:22     Gate FAIL | Improve FAIL cur=1.7755 req<=1.7342 prev=1.7696 | Consist ok
2026-05-24 10:33:22 ema_cur=1.8582 ema_next=1.9043 ratio=1.025 max<=1.20
2026-05-24 10:33:23   Evicted cached model:
2026-05-24 10:33:23 galuis116/evolai-future@7f5fd96012be5ad46b4bb52d24f6f07211f16492
2026-05-24 10:33:24   [44/50] UID 94 | mrthor102/evolai-tfm-super-001 @
2026-05-24 10:33:24 f612e4215b95fc309311d8b27cfba516801d6000 | hotkey 5CPXihPMoGQ2…
2026-05-24 10:33:24     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:33:24    Downloading
2026-05-24 10:33:24 clear-blue-sky/evolai-reborn-tfm-005@0b4c59d6e8333ae1e26b86eccebe612ed58f302a…
2026-05-24 10:33:24     Fetched 20 texts (20 indices)
2026-05-24 10:33:25     Loaded (local prefetch)
2026-05-24 10:33:26     Model 0.46B → batch=512, seq=16384
2026-05-24 10:33:28    Ready:
2026-05-24 10:33:28 clear-blue-sky/evolai-reborn-tfm-005@0b4c59d6e8333ae1e26b86eccebe612ed58f302a
2026-05-24 10:34:04     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 10:34:05     Loss 4.0298 | Size ×0.50 | Think 4.0298 | ThinkGain 0 (+0.4608) | Flow
2026-05-24 10:34:05 0.0000 | KL 2.1427 | NextKL 2.1725 | SideQ 0% | Score 0.0000 (38.9s)
2026-05-24 10:34:05     Gate FAIL | Improve FAIL cur=2.1427 req<=2.0885 prev=2.1311 | Consist ok
2026-05-24 10:34:05 ema_cur=1.9326 ema_next=1.9667 ratio=1.018 max<=1.20
2026-05-24 10:34:06   Evicted cached model:
2026-05-24 10:34:06 mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba
2026-05-24 10:34:07   [45/50] UID 72 | clear-blue-sky/evolai-reborn-tfm-010 @
2026-05-24 10:34:07 1533efda6c349e0b8dcc31b24b2ca15670c5da45 | hotkey 5H3rMcqJQcbK…
2026-05-24 10:34:07     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:34:07    Downloading
2026-05-24 10:34:07 logosnodos/evolai-qwen-1.5b@7e121e8efe6c6b93d622e9a53972d221e763d10b…
2026-05-24 10:34:07     Fetched 20 texts (20 indices)
2026-05-24 10:34:08     Loaded (local prefetch)
2026-05-24 10:34:09     Model 0.46B → batch=512, seq=16384
2026-05-24 10:34:51     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:39
2026-05-24 10:34:51     Loss 3.7956 | Size ×0.50 | Think 3.7956 | ThinkGain 0 (+0.4589) | Flow
2026-05-24 10:34:51 0.0840 | KL 1.8710 | NextKL 1.7265 | SideQ 0% | Score 0.0000 (42.1s)
2026-05-24 10:34:51     Gate FAIL | Improve FAIL cur=1.8710 req<=1.8129 prev=1.8499 | Consist ok
2026-05-24 10:34:51 ema_cur=1.8902 ema_next=1.8873 ratio=0.998 max<=1.20
2026-05-24 10:34:53   Evicted cached model:
2026-05-24 10:34:53 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb
2026-05-24 10:34:54   [46/50] UID 83 | clear-blue-sky/evolai-reborn-tfm-005 @
2026-05-24 10:34:54 0b4c59d6e8333ae1e26b86eccebe612ed58f302a | hotkey 5G8tRiKdn5cC…
2026-05-24 10:34:54     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:34:54     Fetched 20 texts (20 indices)
2026-05-24 10:34:54    Ready: logosnodos/evolai-qwen-1.5b@7e121e8efe6c6b93d622e9a53972d221e763d10b
2026-05-24 10:34:54    Downloading Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4…
2026-05-24 10:34:56     Loaded (local prefetch)
2026-05-24 10:34:56     Model 0.46B → batch=512, seq=16384
2026-05-24 10:34:57    Ready: Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4
2026-05-24 10:35:34     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:35:34     Loss 3.6483 | Size ×0.50 | Think 3.6483 | ThinkGain 0 (+0.4621) | Flow
2026-05-24 10:35:34 0.0000 | KL 1.7435 | NextKL 1.9762 | SideQ 0% | Score 0.0000 (38.1s)
2026-05-24 10:35:34     Gate FAIL | Improve FAIL cur=1.7435 req<=1.6958 prev=1.7304 | Consist ok
2026-05-24 10:35:34 ema_cur=2.3962 ema_next=1.9221 ratio=0.802 max<=1.20
2026-05-24 10:35:36   Evicted cached model:
2026-05-24 10:35:36 Phoenix9781/evolai-tf-model@b05038fcfdcc79fa8d8e79730074b65cd68c73f9
2026-05-24 10:35:36   [47/50] UID 61 | logosnodos/evolai-qwen-1.5b @
2026-05-24 10:35:36 7e121e8efe6c6b93d622e9a53972d221e763d10b | hotkey 5FNTU6ZYgKup…
2026-05-24 10:35:36     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:35:36     Fetched 20 texts (20 indices)
2026-05-24 10:35:36    Downloading
2026-05-24 10:35:36 mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678…
2026-05-24 10:35:38     Loaded (local prefetch)
2026-05-24 10:35:40    Ready: mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678
2026-05-24 10:35:42     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:35:44   [48/50] UID 92 | Lin2es/evolai-tfm-04o @
2026-05-24 10:35:44 52061d203723fdc8be09324d0c827898fcb7bdc4 | hotkey 5GefYX69KUVQ…
2026-05-24 10:35:44     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:35:44     Fetched 20 texts (20 indices)
2026-05-24 10:35:44    Downloading Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59…
2026-05-24 10:35:45     Loaded (local prefetch)
2026-05-24 10:35:45     Model 0.46B → batch=512, seq=16384
2026-05-24 10:35:47    Ready: Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59
2026-05-24 10:36:25     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 10:36:25     Loss 2.4898 | Size ×0.50 | Think 2.4898 | ThinkGain 0 (+0.4466) | Flow
2026-05-24 10:36:25 0.0000 | KL 2.7603 | NextKL 2.6926 | SideQ 0% | Score 0.0000 (39.7s)
2026-05-24 10:36:25     Gate FAIL | Improve same SHA cur=2.7603 req<=2.7051 prev=2.7603 | Consist ok
2026-05-24 10:36:25 ema_cur=2.9868 ema_next=2.5750 ratio=0.862 max<=1.20
2026-05-24 10:36:27   Evicted cached model:
2026-05-24 10:36:27 Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600
2026-05-24 10:36:28   [49/50] UID 42 | mihai-777/evolai-tfm-1p5b-v5 @
2026-05-24 10:36:28 bd42aeb0828dfa0126f7fc825e13b49209fec678 | hotkey 5C5WCYnsrXRz…
2026-05-24 10:36:28     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:36:28     Fetched 20 texts (20 indices)
2026-05-24 10:36:29     Loaded (local prefetch)
2026-05-24 10:36:29     Model 0.46B → batch=512, seq=16384
2026-05-24 10:37:07     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:37:08     Loss 3.1298 | Size ×0.50 | Think 3.1298 | ThinkGain 0 (+0.4547) | Flow
2026-05-24 10:37:08 0.2381 | KL 2.4866 | NextKL 2.3438 | SideQ 0% | Score 0.0000 (37.9s)
2026-05-24 10:37:08     Gate FAIL | Improve same SHA cur=2.4866 req<=2.4368 prev=2.4866 | Consist ok
2026-05-24 10:37:08 ema_cur=2.4193 ema_next=2.4211 ratio=1.001 max<=1.20
2026-05-24 10:37:09   Evicted cached model:
2026-05-24 10:37:09 clear-blue-sky/evolai-reborn-tfm-009@461d465d0b0eae7c262990b9a8e3aa112f199ce2
2026-05-24 10:37:10   [50/50] UID 78 | Lin2es/evolai-tfm-02o @
2026-05-24 10:37:10 fc5fc3ee4a3877b825b404dc85c9367c1f248c59 | hotkey 5FA2kgLNs36d…
2026-05-24 10:37:10     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:37:10     Fetched 20 texts (20 indices)
2026-05-24 10:37:12     Loaded (local prefetch)
2026-05-24 10:37:12     Model 0.46B → batch=512, seq=16384
2026-05-24 10:37:51     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 10:37:51     Loss 3.2587 | Size ×0.50 | Think 3.2587 | ThinkGain 0 (+0.4293) | Flow
2026-05-24 10:37:51 0.0000 | KL 2.9689 | NextKL 2.4454 | SideQ 0% | Score 0.0000 (39.4s)
2026-05-24 10:37:51     Gate FAIL | Improve same SHA cur=2.9689 req<=2.9095 prev=2.9689 | Consist ok
2026-05-24 10:37:51 ema_cur=2.8310 ema_next=2.7900 ratio=0.986 max<=1.20
2026-05-24 10:37:53   Evicted cached model:
2026-05-24 10:37:53 mrthor102/evolai-tfm-super-002@00a41f63a194a32daf3fcc2d6d130cbf8260880e
2026-05-24 10:37:54   Cached next refs for transformer: 50 miner(s)
2026-05-24 10:37:54 
2026-05-24 10:37:54   ✓ TRANSFORMER: 30 evaluated, 23 skipped —
2026-05-24 10:37:54 epoch_22925_transformer_20260524_101129.json
2026-05-24 10:37:55   ✓ Telemetry sent (30 records)
2026-05-24 10:37:55 Evaluating MAMBA2 track…
2026-05-24 10:37:55 
2026-05-24 10:37:55   Found 15 locked mamba2 miners
2026-05-24 10:37:55    Downloading Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0…
2026-05-24 10:37:55 Pre-building current/next challenges for 15 miners…
2026-05-24 10:37:55 Fetching 7 files: 100%|██████████| 7/7 [00:02<00:00,  2.45it/s]
2026-05-24 10:37:58    Ready: Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0
2026-05-24 10:37:58    Downloading
2026-05-24 10:37:58 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c…
2026-05-24 10:37:58 Fetching 7 files: 100%|██████████| 7/7 [00:03<00:00,  2.02it/s]
2026-05-24 10:38:02    Ready:
2026-05-24 10:38:02 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c
2026-05-24 10:38:15 ✓ Ref data ready: submitted=15, cached=15
2026-05-24 10:38:15   [1/15] UID 11 | Lin2es/evolai-mb2-01v @
2026-05-24 10:38:15 a7f32e5ce7f8d307c98560e5025525f3703310c0 | hotkey 5HYuS4jrJJ56…
2026-05-24 10:38:15     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:38:15     Fetched 20 texts (20 indices)
2026-05-24 10:38:15    Downloading
2026-05-24 10:38:15 Radiant28/evolai-mamba2-0.47b-v3@97f692fb0b295aa29075d3f9d592bfb4e7625b16…
2026-05-24 10:38:16     Loaded (local prefetch)
2026-05-24 10:38:16     Model 0.48B → batch=512, seq=16384
2026-05-24 10:38:18    Ready:
2026-05-24 10:38:18 Radiant28/evolai-mamba2-0.47b-v3@97f692fb0b295aa29075d3f9d592bfb4e7625b16
2026-05-24 10:38:26     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:02
2026-05-24 10:38:26     Loss 4.7065 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:38:26 0.0000 | KL 4.7065 | NextKL 4.6076 | SideQ 0% | Score 0.0000 (9.6s)
2026-05-24 10:38:26     Gate FAIL | Improve same SHA cur=4.7065 req<=4.6124 prev=4.7065 | Consist ok
2026-05-24 10:38:26 ema_cur=4.6666 ema_next=4.6670 ratio=1.000 max<=1.20
2026-05-24 10:38:27   Evicted cached model:
2026-05-24 10:38:27 clear-blue-sky/evolai-reborn-tfm-003@efc7fcf7302b03d8ad811f87aceb8095dd43ddc1
2026-05-24 10:38:28   [2/15] UID 32 | mihai-777/evolai-mamba2-1p6b-alt @
2026-05-24 10:38:28 131bd3907f9816bbf184f5651ba63af66046e84c | hotkey 5GL84HKDau7C…
2026-05-24 10:38:28     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:38:28     Fetched 20 texts (20 indices)
2026-05-24 10:38:28    Downloading Lin2es/evolai-mb2-04v@9c0198682f16cc8595fec849aa37227f7160e92c…
2026-05-24 10:38:30     Loaded (local prefetch)
2026-05-24 10:38:30     Model 0.48B → batch=512, seq=16384
2026-05-24 10:38:31    Ready: Lin2es/evolai-mb2-04v@9c0198682f16cc8595fec849aa37227f7160e92c
2026-05-24 10:38:39     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:03
2026-05-24 10:38:39     Loss 4.8377 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:38:39 0.1327 | KL 4.8377 | NextKL 4.8200 | SideQ 0% | Score 0.0000 (9.1s)
2026-05-24 10:38:39     Gate FAIL | Improve same SHA cur=4.8377 req<=4.7409 prev=4.8377 | Consist ok
2026-05-24 10:38:39 ema_cur=4.8755 ema_next=4.8628 ratio=0.997 max<=1.20
2026-05-24 10:38:41   Evicted cached model:
2026-05-24 10:38:41 mrthor102/evolai-tfm-super-001@f612e4215b95fc309311d8b27cfba516801d6000
2026-05-24 10:38:42   [3/15] UID 41 | Radiant28/evolai-mamba2-0.47b-v3 @
2026-05-24 10:38:42 97f692fb0b295aa29075d3f9d592bfb4e7625b16 | hotkey 5CP5QrWuFe93…
2026-05-24 10:38:42     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:38:42     Fetched 20 texts (20 indices)
2026-05-24 10:38:42    Downloading
2026-05-24 10:38:42 evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a…
2026-05-24 10:38:43     Loaded (local prefetch)
2026-05-24 10:38:43     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 10:38:46   [4/15] UID 89 | Lin2es/evolai-mb2-04v @
2026-05-24 10:38:46 9c0198682f16cc8595fec849aa37227f7160e92c | hotkey 5DkZf6V3X8Za…
2026-05-24 10:38:46     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:38:46     Fetched 20 texts (20 indices)
2026-05-24 10:38:46    Ready: evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a
2026-05-24 10:38:46    Downloading Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8…
2026-05-24 10:38:47     Loaded (local prefetch)
2026-05-24 10:38:48     ⚠ Vocab incompatible (model=151665 < ref=248077) — skipping
2026-05-24 10:38:48    Ready: Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8
2026-05-24 10:38:49   [5/15] UID 96 | evolai/evolai_mamba_naive_kl @
2026-05-24 10:38:49 b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a | hotkey 5HQuJVXBXGrW…
2026-05-24 10:38:49     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:38:49     Fetched 20 texts (20 indices)
2026-05-24 10:38:49    Downloading
2026-05-24 10:38:49 elgin-group/evolai-mamba2-0p47b-v1@39b2f90ad08643d34503c88f5c7224fd3dabeed7…
2026-05-24 10:38:51     Loaded (local prefetch)
2026-05-24 10:38:51     Model 0.46B → batch=512, seq=16384
2026-05-24 10:38:52    Ready:
2026-05-24 10:38:52 elgin-group/evolai-mamba2-0p47b-v1@39b2f90ad08643d34503c88f5c7224fd3dabeed7
2026-05-24 10:38:55     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 10:38:55     Loss 3.7662 | Size ×0.50 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:38:55 0.0000 | KL 3.7662 | NextKL 3.6308 | SideQ 0% | Score 0.0000 (3.8s)
2026-05-24 10:38:55     Gate FAIL | Improve same SHA cur=3.7662 req<=3.6909 prev=3.7662 | Consist ok
2026-05-24 10:38:55 ema_cur=3.8837 ema_next=3.5172 ratio=0.906 max<=1.20
2026-05-24 10:38:56   Evicted cached model:
2026-05-24 10:38:56 clear-blue-sky/evolai-reborn-tfm-010@1533efda6c349e0b8dcc31b24b2ca15670c5da45
2026-05-24 10:38:57   [6/15] UID 90 | Lin2es/evolai-mb2-02v @
2026-05-24 10:38:57 c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8 | hotkey 5CtLLhrw6Lxa…
2026-05-24 10:38:57    Downloading Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd…
2026-05-24 10:38:57     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:38:57     Fetched 20 texts (20 indices)
2026-05-24 10:38:58     Loaded (local prefetch)
2026-05-24 10:38:59     Model 0.48B → batch=512, seq=16384
2026-05-24 10:39:00    Ready: Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd
2026-05-24 10:39:02     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 10:39:03     Loss 4.7924 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:39:03 0.0000 | KL 4.7924 | NextKL 4.6488 | SideQ 0% | Score 0.0000 (3.9s)
2026-05-24 10:39:03     Gate FAIL | Improve same SHA cur=4.7924 req<=4.6965 prev=4.7924 | Consist ok
2026-05-24 10:39:03 ema_cur=5.0297 ema_next=4.7107 ratio=0.937 max<=1.20
2026-05-24 10:39:05   Evicted cached model:
2026-05-24 10:39:05 clear-blue-sky/evolai-reborn-tfm-005@0b4c59d6e8333ae1e26b86eccebe612ed58f302a
2026-05-24 10:39:05   [7/15] UID 34 | elgin-group/evolai-mamba2-0p47b-v1 @
2026-05-24 10:39:05 39b2f90ad08643d34503c88f5c7224fd3dabeed7 | hotkey 5GNJr9NfE9e9…
2026-05-24 10:39:05    Downloading
2026-05-24 10:39:05 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518…
2026-05-24 10:39:05     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:39:05     Fetched 20 texts (20 indices)
2026-05-24 10:39:06     Loaded (local prefetch)
2026-05-24 10:39:06     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 10:39:08   [8/15] UID 91 | Lin2es/evolai-mb2-03v @
2026-05-24 10:39:08 3047597c4e4b4430450ddcd633240b88d781fdbd | hotkey 5EcdUqvUBCSp…
2026-05-24 10:39:08     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:39:08     Fetched 20 texts (20 indices)
2026-05-24 10:39:08    Ready:
2026-05-24 10:39:08 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518
2026-05-24 10:39:08    Downloading
2026-05-24 10:39:08 andrebarrosilva1123/evolai-mamba2-a@55b92d373b1c219a4cfbac7034c154ddbcdc854d…
2026-05-24 10:39:09     Loaded (local prefetch)
2026-05-24 10:39:10     Model 0.48B → batch=512, seq=16384
2026-05-24 10:39:11    Ready:
2026-05-24 10:39:11 andrebarrosilva1123/evolai-mamba2-a@55b92d373b1c219a4cfbac7034c154ddbcdc854d
2026-05-24 10:39:14     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 10:39:14     Loss 4.5906 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:39:14 0.0873 | KL 4.5906 | NextKL 4.5813 | SideQ 0% | Score 0.0000 (4.0s)
2026-05-24 10:39:14     Gate FAIL | Improve same SHA cur=4.5906 req<=4.4988 prev=4.5906 | Consist ok
2026-05-24 10:39:14 ema_cur=4.6575 ema_next=4.6522 ratio=0.999 max<=1.20
2026-05-24 10:39:15   Evicted cached model:
2026-05-24 10:39:15 Lin2es/evolai-tfm-04o@52061d203723fdc8be09324d0c827898fcb7bdc4
2026-05-24 10:39:16   [9/15] UID 30 | mihai-777/evolai-mamba2-0p47b-v3 @
2026-05-24 10:39:16 c2a96b92acf632d51a2c21da4482f77f98256518 | hotkey 5GGsbuVKDrTA…
2026-05-24 10:39:16     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:39:16     Fetched 20 texts (20 indices)
2026-05-24 10:39:16    Downloading
2026-05-24 10:39:16 andrebarrosilva1123/evolai-mamba2-c@dc37c985d66c77e3d10bf9eaf16e6dc952c62e17…
2026-05-24 10:39:17     Loaded (local prefetch)
2026-05-24 10:39:18     Model 0.48B → batch=512, seq=16384
2026-05-24 10:39:19    Ready:
2026-05-24 10:39:19 andrebarrosilva1123/evolai-mamba2-c@dc37c985d66c77e3d10bf9eaf16e6dc952c62e17
2026-05-24 10:39:22     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 10:39:22     Loss 4.8142 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:39:22 0.2754 | KL 4.8142 | NextKL 4.9009 | SideQ 0% | Score 0.0000 (4.0s)
2026-05-24 10:39:22     Gate FAIL | Improve same SHA cur=4.8142 req<=4.7179 prev=4.8142 | Consist ok
2026-05-24 10:39:22 ema_cur=4.7735 ema_next=4.7905 ratio=1.004 max<=1.20
2026-05-24 10:39:23   Evicted cached model:
2026-05-24 10:39:23 mihai-777/evolai-tfm-1p5b-v5@bd42aeb0828dfa0126f7fc825e13b49209fec678
2026-05-24 10:39:24   [10/15] UID 56 | andrebarrosilva1123/evolai-mamba2-a @
2026-05-24 10:39:24 55b92d373b1c219a4cfbac7034c154ddbcdc854d | hotkey 5D1zGn2n3mzF…
2026-05-24 10:39:24     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:39:24    Downloading
2026-05-24 10:39:24 Radiant28/evolai-mamba2-0.47b-v2@475bf7bf65af1192ed824d58816c1d83f3475983…
2026-05-24 10:39:24     Fetched 20 texts (20 indices)
2026-05-24 10:39:25     Loaded (local prefetch)
2026-05-24 10:39:25     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 10:39:27   [11/15] UID 58 | andrebarrosilva1123/evolai-mamba2-c @
2026-05-24 10:39:27 dc37c985d66c77e3d10bf9eaf16e6dc952c62e17 | hotkey 5EgtSzXJbjpV…
2026-05-24 10:39:27     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:39:27     Fetched 20 texts (20 indices)
2026-05-24 10:39:27    Ready:
2026-05-24 10:39:27 Radiant28/evolai-mamba2-0.47b-v2@475bf7bf65af1192ed824d58816c1d83f3475983
2026-05-24 10:39:27    Downloading
2026-05-24 10:39:27 batster4/evolai-mamba2-v1@142f14d218be618e3161d86926085b3a9cefed55…
2026-05-24 10:39:29     Loaded (local prefetch)
2026-05-24 10:39:29     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 10:39:31   [12/15] UID 39 | Radiant28/evolai-mamba2-0.47b-v2 @
2026-05-24 10:39:31 475bf7bf65af1192ed824d58816c1d83f3475983 | hotkey 5FvTt3gVVhFT…
2026-05-24 10:39:31     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:39:31     Fetched 20 texts (20 indices)
2026-05-24 10:39:31    Ready: batster4/evolai-mamba2-v1@142f14d218be618e3161d86926085b3a9cefed55
2026-05-24 10:39:31    Downloading
2026-05-24 10:39:31 mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7…
2026-05-24 10:39:32     Loaded (local prefetch)
2026-05-24 10:39:33     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 10:39:34   [13/15] UID 60 | batster4/evolai-mamba2-v1 @
2026-05-24 10:39:34 142f14d218be618e3161d86926085b3a9cefed55 | hotkey 5Dc8EpAixcqc…
2026-05-24 10:39:34     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:39:34     Fetched 20 texts (20 indices)
2026-05-24 10:39:34    Ready: mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7
2026-05-24 10:39:34    Downloading
2026-05-24 10:39:34 andrebarrosilva1123/evolai-mamba2-b@62336a49df6d6014f779575adfd29373c228edd4…
2026-05-24 10:39:36     Loaded (local prefetch)
2026-05-24 10:39:36     ⚠ Invalid model size (0.82B; allowed 0.45-0.48B, 1.50-1.80B) — skipping
2026-05-24 10:39:37    Ready:
2026-05-24 10:39:37 andrebarrosilva1123/evolai-mamba2-b@62336a49df6d6014f779575adfd29373c228edd4
2026-05-24 10:39:38   [14/15] UID 31 | mihai-777/evolai-mamba2-0p47b @
2026-05-24 10:39:38 7b6564c9a46f602702c260185aa43867f321dee7 | hotkey 5CJuKKq16FkR…
2026-05-24 10:39:38     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:39:38     Fetched 20 texts (20 indices)
2026-05-24 10:39:39     Loaded (local prefetch)
2026-05-24 10:39:39     Model 0.48B → batch=512, seq=16384
2026-05-24 10:39:43     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:01
2026-05-24 10:39:44     Loss 4.8298 | Size ×0.52 | Think 0.0000 | ThinkGain 0 (+0.5000) | Flow
2026-05-24 10:39:44 0.0000 | KL 4.8298 | NextKL 4.8128 | SideQ 0% | Score 0.0000 (4.0s)
2026-05-24 10:39:44     Gate FAIL | Improve same SHA cur=4.8298 req<=4.7332 prev=4.8298 | Consist ok
2026-05-24 10:39:44 ema_cur=4.7831 ema_next=4.7822 ratio=1.000 max<=1.20
2026-05-24 10:39:45   Evicted cached model:
2026-05-24 10:39:45 Lin2es/evolai-tfm-02o@fc5fc3ee4a3877b825b404dc85c9367c1f248c59
2026-05-24 10:39:46   [15/15] UID 57 | andrebarrosilva1123/evolai-mamba2-b @
2026-05-24 10:39:46 62336a49df6d6014f779575adfd29373c228edd4 | hotkey 5EZx1DRvpMGK…
2026-05-24 10:39:46     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:39:46     Fetched 20 texts (20 indices)
2026-05-24 10:39:47     Loaded (local prefetch)
2026-05-24 10:39:47     ⚠ Vocab incompatible (model=151669 < ref=248077) — skipping
2026-05-24 10:39:49   Cached next refs for mamba2: 15 miner(s)
2026-05-24 10:39:49 
2026-05-24 10:39:49   ✓ MAMBA2: 7 evaluated, 14 skipped — epoch_22925_mamba2_20260524_101129.json
2026-05-24 10:39:49   ✓ Telemetry sent (7 records)
2026-05-24 10:39:49 Current Leaderboard:
2026-05-24 10:40:04 
2026-05-24 10:40:04 TRANSFORMER
2026-05-24 10:40:04 ┏━━━━━━┳━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━━━┳━━━━━━━┓
2026-05-24 10:40:04 ┃      ┃     ┃        ┃     Latest ┃           ┃       ┃     ┃         ┃       ┃
2026-05-24 10:40:04 ┃ Rank ┃ UID ┃  Score ┃       Loss ┃ ThinkGain ┃  Flow ┃ SQ% ┃      KL ┃ Evals ┃
2026-05-24 10:40:04 ┡━━━━━━╇━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━━━╇━━━━━━━┩
2026-05-24 10:40:04 │    1 │   8 │ 0.0305 │     4.0088 │  0 FAIL   │ 0.000 │  0% │  1.6860 │   311 │
2026-05-24 10:40:04 │    2 │  48 │ 0.0001 │     4.0362 │  0 FAIL   │ 0.159 │  0% │  2.2124 │   135 │
2026-05-24 10:40:04 │    3 │  82 │ 0.0000 │     3.9337 │  0 FAIL   │ 0.425 │  0% │  1.7755 │   346 │
2026-05-24 10:40:04 │    4 │  66 │ 0.0000 │     3.5299 │  0 FAIL   │ 0.066 │  0% │  1.8533 │   346 │
2026-05-24 10:40:04 │    5 │  87 │ 0.0000 │     4.0577 │  0 FAIL   │ 0.133 │  0% │  2.2495 │   147 │
2026-05-24 10:40:04 │    6 │  86 │ 0.0000 │     4.1094 │  0 FAIL   │ 0.139 │  0% │  2.3171 │   148 │
2026-05-24 10:40:04 │    7 │  73 │ 0.0000 │     3.9111 │  0 FAIL   │ 0.000 │  0% │  1.8439 │   131 │
2026-05-24 10:40:04 │    8 │  93 │ 0.0000 │     3.8161 │  0 FAIL   │ 0.000 │  0% │  2.0005 │   131 │
2026-05-24 10:40:04 │    9 │  97 │ 0.0000 │     3.8636 │  0 FAIL   │ 0.000 │  0% │  1.9914 │   261 │
2026-05-24 10:40:04 │   10 │  67 │ 0.0000 │     3.6214 │  0 FAIL   │ 0.513 │  0% │  1.8223 │   348 │
2026-05-24 10:40:04 │   11 │  70 │ 0.0000 │     3.5738 │  0 FAIL   │ 0.000 │  0% │  2.0589 │   346 │
2026-05-24 10:40:04 │   12 │  83 │ 0.0000 │     3.6483 │  0 FAIL   │ 0.000 │  0% │  1.7435 │   348 │
2026-05-24 10:40:04 │   13 │  85 │ 0.0000 │     3.5537 │  0 FAIL   │ 0.000 │  0% │  1.8171 │   335 │
2026-05-24 10:40:04 │   14 │  99 │ 0.0000 │     3.7980 │  0 FAIL   │ 0.000 │  0% │  1.8333 │   129 │
2026-05-24 10:40:04 │   15 │  72 │ 0.0000 │     3.7956 │  0 FAIL   │ 0.084 │  0% │  1.8710 │   130 │
2026-05-24 10:40:04 │   16 │  62 │ 0.0000 │     3.8257 │  0 FAIL   │ 0.000 │  0% │  2.0294 │   348 │
2026-05-24 10:40:04 │   17 │  94 │ 0.0000 │     4.0298 │  0 FAIL   │ 0.000 │  0% │  2.1427 │   261 │
2026-05-24 10:40:04 │   18 │  98 │ 0.0000 │     3.8191 │  0 FAIL   │ 0.000 │  0% │  1.7783 │   260 │
2026-05-24 10:40:04 │   19 │  69 │ 0.0000 │     3.4951 │  0 FAIL   │ 0.224 │  0% │  1.7200 │   131 │
2026-05-24 10:40:04 │   20 │   9 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   350 │
2026-05-24 10:40:04 │   21 │  25 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:40:04 │   22 │  33 │ 0.0000 │     2.9179 │  0 FAIL   │ 0.000 │  0% │  2.6364 │   348 │
2026-05-24 10:40:04 │   23 │  35 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 10:40:04 │   24 │  36 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:40:04 │   25 │  37 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 10:40:04 │   26 │  38 │ 0.0000 │     3.2578 │  0 FAIL   │ 0.000 │  0% │  2.5457 │   347 │
2026-05-24 10:40:04 │   27 │  40 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 10:40:04 │   28 │  42 │ 0.0000 │     3.1298 │  0 FAIL   │ 0.238 │  0% │  2.4866 │   348 │
2026-05-24 10:40:04 │   29 │  43 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 10:40:04 │   30 │  44 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   349 │
2026-05-24 10:40:04 │   31 │  45 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 10:40:04 │   32 │  49 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:40:04 │   33 │  50 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   347 │
2026-05-24 10:40:04 │   34 │  51 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   320 │
2026-05-24 10:40:04 │   35 │  52 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   321 │
2026-05-24 10:40:04 │   36 │  53 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 10:40:04 │   37 │  54 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   319 │
2026-05-24 10:40:04 │   38 │  55 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   351 │
2026-05-24 10:40:04 │   39 │  59 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 10:40:04 │   40 │  61 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 10:40:04 │   41 │  65 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   348 │
2026-05-24 10:40:04 │   42 │  75 │ 0.0000 │     3.3909 │  0 FAIL   │ 0.000 │  0% │  2.8338 │   349 │
2026-05-24 10:40:04 │   43 │  76 │ 0.0000 │     2.4060 │  0 FAIL   │ 0.110 │  0% │  2.4715 │   347 │
2026-05-24 10:40:04 │   44 │  77 │ 0.0000 │     3.3423 │  0 FAIL   │ 0.000 │  0% │  2.9899 │   250 │
2026-05-24 10:40:04 │   45 │  78 │ 0.0000 │     3.2587 │  0 FAIL   │ 0.000 │  0% │  2.9689 │   250 │
2026-05-24 10:40:04 │   46 │  79 │ 0.0000 │     1.9053 │  0 FAIL   │ 0.031 │  0% │  2.3064 │   250 │
2026-05-24 10:40:04 │   47 │  80 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   349 │
2026-05-24 10:40:04 │   48 │  84 │ 0.0000 │     3.9502 │  0 FAIL   │ 0.000 │  0% │  1.9489 │   332 │
2026-05-24 10:40:04 │   49 │  88 │ 0.0000 │     3.9147 │  0 FAIL   │ 0.290 │  0% │  1.9992 │   146 │
2026-05-24 10:40:04 │   50 │  92 │ 0.0000 │     2.4898 │  0 FAIL   │ 0.000 │  0% │  2.7603 │   251 │
2026-05-24 10:40:04 │   51 │  95 │ 0.0000 │     2.9910 │  0 FAIL   │ 0.219 │  0% │  3.0063 │   260 │
2026-05-24 10:40:04 │   52 │ 100 │ 0.0000 │     3.6608 │  0 FAIL   │ 0.000 │  0% │  3.8609 │   259 │
2026-05-24 10:40:04 │   53 │ 101 │ 0.0000 │     3.6152 │  0 FAIL   │ 0.356 │  0% │  1.9061 │    81 │
2026-05-24 10:40:04 └──────┴─────┴────────┴────────────┴───────────┴───────┴─────┴─────────┴───────┘
2026-05-24 10:40:04 
2026-05-24 10:40:04 MAMBA2
2026-05-24 10:40:04 ┏━━━━━━┳━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━━━┳━━━━━━━┓
2026-05-24 10:40:04 ┃      ┃     ┃        ┃     Latest ┃           ┃       ┃     ┃         ┃       ┃
2026-05-24 10:40:04 ┃ Rank ┃ UID ┃  Score ┃       Loss ┃ ThinkGain ┃  Flow ┃ SQ% ┃      KL ┃ Evals ┃
2026-05-24 10:40:04 ┡━━━━━━╇━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━━━╇━━━━━━━┩
2026-05-24 10:40:04 │    1 │  11 │ 0.0000 │     4.7065 │  0 FAIL   │ 0.000 │  0% │  4.7065 │   250 │
2026-05-24 10:40:04 │    2 │  30 │ 0.0000 │     4.8142 │  0 FAIL   │ 0.275 │  0% │  4.8142 │   345 │
2026-05-24 10:40:04 │    3 │  31 │ 0.0000 │     4.8298 │  0 FAIL   │ 0.000 │  0% │  4.8298 │   345 │
2026-05-24 10:40:04 │    4 │  32 │ 0.0000 │     4.8377 │  0 FAIL   │ 0.133 │  0% │  4.8377 │   345 │
2026-05-24 10:40:04 │    5 │  34 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 10:40:04 │    6 │  39 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   346 │
2026-05-24 10:40:04 │    7 │  41 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 10:40:04 │    8 │  56 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 10:40:04 │    9 │  57 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 10:40:04 │   10 │  58 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 10:40:04 │   11 │  60 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   345 │
2026-05-24 10:40:04 │   12 │  63 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   271 │
2026-05-24 10:40:04 │   13 │  64 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 10:40:04 │   14 │  68 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 10:40:04 │   15 │  71 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   271 │
2026-05-24 10:40:04 │   16 │  74 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   272 │
2026-05-24 10:40:04 │   17 │  81 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   273 │
2026-05-24 10:40:04 │   18 │  89 │ 0.0000 │    10.0000 │  0 FAIL   │ 0.000 │  0% │ 10.0000 │   250 │
2026-05-24 10:40:04 │   19 │  90 │ 0.0000 │     4.7924 │  0 FAIL   │ 0.000 │  0% │  4.7924 │   260 │
2026-05-24 10:40:04 │   20 │  91 │ 0.0000 │     4.5906 │  0 FAIL   │ 0.087 │  0% │  4.5906 │   260 │
2026-05-24 10:40:04 │   21 │  96 │ 0.0000 │     3.7662 │  0 FAIL   │ 0.000 │  0% │  3.7662 │   260 │
2026-05-24 10:40:04 └──────┴─────┴────────┴────────────┴───────────┴───────┴─────┴─────────┴───────┘
2026-05-24 10:40:04 
2026-05-24 10:40:04 Round complete in epoch 22925 (1715s elapsed). Starting next round immediately…
2026-05-24 10:40:04 
2026-05-24 10:40:04 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2026-05-24 10:40:04 
2026-05-24 10:40:04 ━━━ Epoch #22926 (Loop #6) ━━━ block=8253411, ~61m remaining
2026-05-24 10:40:13 
2026-05-24 10:40:13   ⚠ UID 86: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:40:13 (Request ID:
2026-05-24 10:40:13 Root=1-6a12d58d-37fa7589044720594796a8e7;557b0b39-e877-4380-978c-d7505287760b)
2026-05-24 10:40:13 
2026-05-24 10:40:13 Repository Not Found for url:
2026-05-24 10:40:13 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-012/revision/main.
2026-05-24 10:40:13 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:40:13 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:40:13 authenticated and your token has the required permissions.
2026-05-24 10:40:13 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:40:13 Invalid username or password.
2026-05-24 10:40:13   ⚠ UID 87: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:40:13 (Request ID:
2026-05-24 10:40:13 Root=1-6a12d58d-1a493d1d42564538329b0477;e1837947-ee1c-4576-a56a-318d11d3997c)
2026-05-24 10:40:13 
2026-05-24 10:40:13 Repository Not Found for url:
2026-05-24 10:40:13 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-013/revision/main.
2026-05-24 10:40:13 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:40:13 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:40:13 authenticated and your token has the required permissions.
2026-05-24 10:40:13 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:40:13 Invalid username or password.
2026-05-24 10:40:13   ⚠ UID 88: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:40:13 (Request ID:
2026-05-24 10:40:13 Root=1-6a12d58d-79374dcf5a749a9f69b53d12;81980aef-a5e9-42c3-b91e-87329e22412a)
2026-05-24 10:40:13 
2026-05-24 10:40:13 Repository Not Found for url:
2026-05-24 10:40:13 https://huggingface.co/api/models/clear-blue-sky/evolai-tfm-014/revision/main.
2026-05-24 10:40:13 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:40:13 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:40:13 authenticated and your token has the required permissions.
2026-05-24 10:40:13 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:40:13 Invalid username or password.
2026-05-24 10:40:14   Locked transformer revisions (50 miner(s), 3 skipped)
2026-05-24 10:40:22   ⚠ UID 63: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:40:22 (Request ID:
2026-05-24 10:40:22 Root=1-6a12d596-0a59a79e5deb7dd07fba8224;1fcb23c5-60eb-411f-a4fd-7d30c2b327c6)
2026-05-24 10:40:22 
2026-05-24 10:40:22 Repository Not Found for url:
2026-05-24 10:40:22 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-009/revision/main.
2026-05-24 10:40:22 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:40:22 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:40:22 authenticated and your token has the required permissions.
2026-05-24 10:40:22 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:40:22 Invalid username or password.
2026-05-24 10:40:22   ⚠ UID 64: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:40:22 (Request ID:
2026-05-24 10:40:22 Root=1-6a12d596-293997d64ecac3ef00eb6370;b4237204-6a38-49d4-aaf1-cb68f4917f59)
2026-05-24 10:40:22 
2026-05-24 10:40:22 Repository Not Found for url:
2026-05-24 10:40:22 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-002/revision/main.
2026-05-24 10:40:22 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:40:22 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:40:22 authenticated and your token has the required permissions.
2026-05-24 10:40:22 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:40:22 Invalid username or password.
2026-05-24 10:40:22   ⚠ UID 68: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:40:22 (Request ID:
2026-05-24 10:40:22 Root=1-6a12d596-2452d26a76e8a20433967a25;1d8934b0-4d5c-43d2-ad61-dec1a8fd6000)
2026-05-24 10:40:22 
2026-05-24 10:40:22 Repository Not Found for url:
2026-05-24 10:40:22 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-008/revision/main.
2026-05-24 10:40:22 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:40:22 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:40:22 authenticated and your token has the required permissions.
2026-05-24 10:40:22 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:40:22 Invalid username or password.
2026-05-24 10:40:22   ⚠ UID 71: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:40:22 (Request ID:
2026-05-24 10:40:22 Root=1-6a12d596-3f4ee95e0bc81a40686b1b8c;d6f99468-1e3d-45d8-aa8b-fcafd64a396b)
2026-05-24 10:40:22 
2026-05-24 10:40:22 Repository Not Found for url:
2026-05-24 10:40:22 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-001/revision/main.
2026-05-24 10:40:22 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:40:22 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:40:22 authenticated and your token has the required permissions.
2026-05-24 10:40:22 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:40:22 Invalid username or password.
2026-05-24 10:40:22   ⚠ UID 74: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:40:22 (Request ID:
2026-05-24 10:40:22 Root=1-6a12d596-557588ce1ecd69eb01ba3026;2b936fff-1bba-4cde-98ef-92bed02b0c8f)
2026-05-24 10:40:22 
2026-05-24 10:40:22 Repository Not Found for url:
2026-05-24 10:40:22 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-007/revision/main.
2026-05-24 10:40:22 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:40:22 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:40:22 authenticated and your token has the required permissions.
2026-05-24 10:40:22 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:40:22 Invalid username or password.
2026-05-24 10:40:22   ⚠ UID 81: revision lock failed: RepositoryNotFoundError: 401 Client Error.
2026-05-24 10:40:22 (Request ID:
2026-05-24 10:40:22 Root=1-6a12d596-2c5a154222d97c741492633a;e8c11e76-388c-46f7-9347-24e6bf19f075)
2026-05-24 10:40:22 
2026-05-24 10:40:22 Repository Not Found for url:
2026-05-24 10:40:22 https://huggingface.co/api/models/clear-blue-sky/evolai-mb2-010/revision/main.
2026-05-24 10:40:22 Please make sure you specified the correct `repo_id` and `repo_type`.
2026-05-24 10:40:22 If you are trying to access a private or gated repo, make sure you are
2026-05-24 10:40:22 authenticated and your token has the required permissions.
2026-05-24 10:40:22 For more details, see https://huggingface.co/docs/huggingface_hub/authentication
2026-05-24 10:40:22 Invalid username or password.
2026-05-24 10:40:22   Locked mamba2 revisions (15 miner(s), 6 skipped)
2026-05-24 10:40:52   Committed round seed epoch=22926 seed=560d0b6e...
2026-05-24 10:40:53 Evaluating TRANSFORMER track…
2026-05-24 10:40:53 
2026-05-24 10:40:53   Found 50 locked transformer miners
2026-05-24 10:40:53    Downloading
2026-05-24 10:40:53 clear-blue-sky/evolai-reborn-tfm-002@445516ade25ae580764f845da0631604e1f2d573…
2026-05-24 10:40:53 Pre-building current/next challenges for 50 miners…
2026-05-24 10:40:53 Fetching 7 files: 100%|██████████| 7/7 [00:04<00:00,  1.69it/s]
2026-05-24 10:40:57    Ready:
2026-05-24 10:40:57 clear-blue-sky/evolai-reborn-tfm-002@445516ade25ae580764f845da0631604e1f2d573
2026-05-24 10:40:57    Downloading
2026-05-24 10:40:57 mrthor102/evolai-tfm-super-001@385ae8ed8a60a825e35a4eeb1f76f948662ae0e2…
2026-05-24 10:40:57 Fetching 7 files: 100%|██████████| 7/7 [00:03<00:00,  1.95it/s]
2026-05-24 10:41:01    Ready:
2026-05-24 10:41:01 mrthor102/evolai-tfm-super-001@385ae8ed8a60a825e35a4eeb1f76f948662ae0e2
2026-05-24 10:41:48 ✓ Ref data ready: submitted=50, cached=50
2026-05-24 10:41:48   [1/50] UID 67 | clear-blue-sky/evolai-reborn-tfm-002 @
2026-05-24 10:41:48 445516ade25ae580764f845da0631604e1f2d573 | hotkey 5GC7k2mkTKGF…
2026-05-24 10:41:48     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:41:48    Downloading
2026-05-24 10:41:48 clear-blue-sky/evolai-reborn-tfm-008@0ef35718add6719e5183c735af3f1f6034c10b7e…
2026-05-24 10:41:48     Fetched 20 texts (20 indices)
2026-05-24 10:41:50     Loaded (local prefetch)
2026-05-24 10:41:50     Model 0.46B → batch=512, seq=16384
2026-05-24 10:41:52    Ready:
2026-05-24 10:41:52 clear-blue-sky/evolai-reborn-tfm-008@0ef35718add6719e5183c735af3f1f6034c10b7e
2026-05-24 10:42:45     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:51
2026-05-24 10:42:45     Loss 3.8147 | Size ×0.50 | Think 3.8147 | ThinkGain 0 (+0.4601) | Flow
2026-05-24 10:42:45 0.5472 | KL 1.8031 | NextKL 1.7182 | SideQ 0% | Score 0.0000 (54.8s)
2026-05-24 10:42:45     Gate FAIL | Improve FAIL cur=1.8031 req<=1.7746 prev=1.8108 | Consist ok
2026-05-24 10:42:45 ema_cur=1.8616 ema_next=1.8473 ratio=0.992 max<=1.20
2026-05-24 10:42:47   Evicted cached model:
2026-05-24 10:42:47 Lin2es/evolai-mb2-01v@a7f32e5ce7f8d307c98560e5025525f3703310c0
2026-05-24 10:42:47   [2/50] UID 94 | mrthor102/evolai-tfm-super-001 @
2026-05-24 10:42:47 385ae8ed8a60a825e35a4eeb1f76f948662ae0e2 | hotkey 5CPXihPMoGQ2…
2026-05-24 10:42:47    Downloading
2026-05-24 10:42:47 clear-blue-sky/evolai-reborn-tfm-005@93513b7b277ea3f3e5b5a4a60f1ae4c88d9c2967…
2026-05-24 10:42:47     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:42:47     Fetched 20 texts (20 indices)
2026-05-24 10:42:50     Loaded (local prefetch)
2026-05-24 10:42:50     Model 0.46B → batch=512, seq=16384
2026-05-24 10:42:51    Ready:
2026-05-24 10:42:51 clear-blue-sky/evolai-reborn-tfm-005@93513b7b277ea3f3e5b5a4a60f1ae4c88d9c2967
2026-05-24 10:43:31    alpha=0.005454 TAO/α  budget=0.049688
2026-05-24 10:43:48    emission scale=1.000 (active miners)
2026-05-24 10:43:48    emission scale=1.000 (active miners)
2026-05-24 10:43:48    all quality scores zero after gates — emission share redistributed to
2026-05-24 10:43:48 productive tracks
2026-05-24 10:43:51   ✓  set at 10:43:51 UTC
2026-05-24 10:43:52     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:57
2026-05-24 10:43:52     Loss 4.0698 | Size ×0.50 | Think 4.0698 | ThinkGain 0 (+0.4614) | Flow
2026-05-24 10:43:52 0.0000 | KL 2.1714 | NextKL 2.0032 | SideQ 0% | Score 0.0000 (61.7s)
2026-05-24 10:43:52     Gate FAIL | Improve FAIL cur=2.1714 req<=2.1290 prev=2.1725 | Consist ok
2026-05-24 10:43:52 ema_cur=1.9564 ema_next=1.9704 ratio=1.007 max<=1.20
2026-05-24 10:43:54   Evicted cached model:
2026-05-24 10:43:54 mihai-777/evolai-mamba2-1p6b-alt@131bd3907f9816bbf184f5651ba63af66046e84c
2026-05-24 10:43:55   [3/50] UID 85 | clear-blue-sky/evolai-reborn-tfm-008 @
2026-05-24 10:43:55 0ef35718add6719e5183c735af3f1f6034c10b7e | hotkey 5EC5MzPj6dGb…
2026-05-24 10:43:55     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:43:55     Fetched 20 texts (20 indices)
2026-05-24 10:43:55    Downloading
2026-05-24 10:43:55 clear-blue-sky/evolai-reborn-tfm-006@75630f5ca4d50de58eadd7c82d62d5e97b9d27be…
2026-05-24 10:43:56     Loaded (local prefetch)
2026-05-24 10:43:57     Model 0.46B → batch=512, seq=16384
2026-05-24 10:43:59    Ready:
2026-05-24 10:43:59 clear-blue-sky/evolai-reborn-tfm-006@75630f5ca4d50de58eadd7c82d62d5e97b9d27be
2026-05-24 10:45:00     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:59
2026-05-24 10:45:00     Loss 3.9702 | Size ×0.50 | Think 3.9702 | ThinkGain 0 (+0.4610) | Flow
2026-05-24 10:45:00 0.0000 | KL 1.7448 | NextKL 1.8624 | SideQ 0% | Score 0.0000 (63.0s)
2026-05-24 10:45:00     Gate FAIL | Improve FAIL cur=1.7448 req<=1.7170 prev=1.7520 | Consist ok
2026-05-24 10:45:00 ema_cur=2.3332 ema_next=1.9092 ratio=0.818 max<=1.20
2026-05-24 10:45:01   Evicted cached model:
2026-05-24 10:45:01 evolai/evolai_mamba_naive_kl@b7c8842d1d5a700bd6a36b834fe6f0b3dc5d321a
2026-05-24 10:45:02   [4/50] UID 83 | clear-blue-sky/evolai-reborn-tfm-005 @
2026-05-24 10:45:02 93513b7b277ea3f3e5b5a4a60f1ae4c88d9c2967 | hotkey 5G8tRiKdn5cC…
2026-05-24 10:45:02     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:45:02     Fetched 20 texts (20 indices)
2026-05-24 10:45:02    Downloading
2026-05-24 10:45:02 andrebarrosilva1123/evolai-b@3414c0abb8793ed4af56fd5e6e536b8b0f5ac520…
2026-05-24 10:45:03     Loaded (local prefetch)
2026-05-24 10:45:04     Model 0.46B → batch=512, seq=16384
2026-05-24 10:45:10    Ready: andrebarrosilva1123/evolai-b@3414c0abb8793ed4af56fd5e6e536b8b0f5ac520
2026-05-24 10:46:05     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 76/76 100% 0:00:57
2026-05-24 10:46:05     Loss 3.6363 | Size ×0.50 | Think 3.6363 | ThinkGain 0 (+0.4634) | Flow
2026-05-24 10:46:05 0.0000 | KL 1.9476 | NextKL 1.8384 | SideQ 0% | Score 0.0000 (61.3s)
2026-05-24 10:46:05     Gate FAIL | Improve FAIL cur=1.9476 req<=1.9367 prev=1.9762 | Consist ok
2026-05-24 10:46:05 ema_cur=2.3513 ema_next=1.9137 ratio=0.814 max<=1.20
2026-05-24 10:46:06   Evicted cached model:
2026-05-24 10:46:06 Lin2es/evolai-mb2-02v@c1ad3d94c5929dcc0e3a40d9d9034bd80da9a1f8
2026-05-24 10:46:07   [5/50] UID 66 | clear-blue-sky/evolai-reborn-tfm-006 @
2026-05-24 10:46:07 75630f5ca4d50de58eadd7c82d62d5e97b9d27be | hotkey 5E4M4B5sVED5…
2026-05-24 10:46:07     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:46:07    Downloading
2026-05-24 10:46:07 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb…
2026-05-24 10:46:07     Fetched 20 texts (20 indices)
2026-05-24 10:46:09     Loaded (local prefetch)
2026-05-24 10:46:09     Model 0.46B → batch=512, seq=16384
2026-05-24 10:46:12    Ready:
2026-05-24 10:46:12 sangerno63/evolai-transformer-v2@4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb
2026-05-24 10:47:14     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:01:00
2026-05-24 10:47:14     Loss 3.8219 | Size ×0.50 | Think 3.8219 | ThinkGain 0 (+0.4627) | Flow
2026-05-24 10:47:14 0.1584 | KL 1.8146 | NextKL 1.9356 | SideQ 0% | Score 0.0000 (64.5s)
2026-05-24 10:47:14     Gate FAIL | Improve FAIL cur=1.8146 req<=1.7824 prev=1.8187 | Consist ok
2026-05-24 10:47:14 ema_cur=1.9391 ema_next=1.9356 ratio=0.998 max<=1.20
2026-05-24 10:47:15   Evicted cached model:
2026-05-24 10:47:15 Lin2es/evolai-mb2-03v@3047597c4e4b4430450ddcd633240b88d781fdbd
2026-05-24 10:47:17   [6/50] UID 50 | andrebarrosilva1123/evolai-b @
2026-05-24 10:47:17 3414c0abb8793ed4af56fd5e6e536b8b0f5ac520 | hotkey 5FXELcBK4WiD…
2026-05-24 10:47:17     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:47:17     Fetched 20 texts (20 indices)
2026-05-24 10:47:17    Downloading
2026-05-24 10:47:17 andrebarrosilva1123/evolai-d@89649e9376dace64f631711d3d270198e376702e…
2026-05-24 10:47:18     Loaded (local prefetch)
2026-05-24 10:47:19     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:47:21   [7/50] UID 48 | sangerno63/evolai-transformer-v2 @
2026-05-24 10:47:21 4b325f440c9ab4b8cc501454c5c5dc5f8e890ebb | hotkey 5ED3KNj5uEVS…
2026-05-24 10:47:21     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:47:21     Fetched 20 texts (20 indices)
2026-05-24 10:47:23     Loaded (local prefetch)
2026-05-24 10:47:23    Ready: andrebarrosilva1123/evolai-d@89649e9376dace64f631711d3d270198e376702e
2026-05-24 10:47:23    Downloading
2026-05-24 10:47:23 mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba…
2026-05-24 10:47:23 Fetching 8 files: 100%|██████████| 8/8 [00:04<00:00,  1.90it/s]
2026-05-24 10:47:24     Model 0.46B → batch=512, seq=16384
2026-05-24 10:47:28    Ready: mihai-777/evolai-tfm-1p5b-05@a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba
2026-05-24 10:48:14     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:47
2026-05-24 10:48:14     Loss 3.8874 | Size ×0.50 | Think 3.8874 | ThinkGain 0 (+0.4438) | Flow
2026-05-24 10:48:14 0.2666 | KL 2.0361 | NextKL 2.1842 | SideQ 0% | Score 0.0001 (50.0s)
2026-05-24 10:48:14     Gate FAIL | Improve same SHA cur=2.0361 req<=1.9953 prev=2.0361 | Consist ok
2026-05-24 10:48:14 ema_cur=2.1714 ema_next=2.1671 ratio=0.998 max<=1.20
2026-05-24 10:48:16   Evicted cached model:
2026-05-24 10:48:16 mihai-777/evolai-mamba2-0p47b-v3@c2a96b92acf632d51a2c21da4482f77f98256518
2026-05-24 10:48:16   [8/50] UID 51 | andrebarrosilva1123/evolai-d @
2026-05-24 10:48:16 89649e9376dace64f631711d3d270198e376702e | hotkey 5EhLiPB1GHwH…
2026-05-24 10:48:16     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:48:16     Fetched 20 texts (20 indices)
2026-05-24 10:48:16    Downloading
2026-05-24 10:48:16 clear-blue-sky/evolai-reborn-tfm-003@ee61abb738c3d06872e7ee8a2c59c7287fbc632c…
2026-05-24 10:48:18     Loaded (local prefetch)
2026-05-24 10:48:19     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:48:21   [9/50] UID 76 | mihai-777/evolai-tfm-1p5b-05 @
2026-05-24 10:48:21 a66a1beeefdbc6ff871ea4854b4e71ed5c3a44ba | hotkey 5GLBxPtoiB7R…
2026-05-24 10:48:21     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:48:21     Fetched 20 texts (20 indices)
2026-05-24 10:48:21    Ready:
2026-05-24 10:48:21 clear-blue-sky/evolai-reborn-tfm-003@ee61abb738c3d06872e7ee8a2c59c7287fbc632c
2026-05-24 10:48:21    Downloading
2026-05-24 10:48:21 Roystar/evolai-qwen2.5-1.5b@47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1…
2026-05-24 10:48:22     Loaded (local prefetch)
2026-05-24 10:48:22     Model 0.46B → batch=512, seq=16384
2026-05-24 10:48:27    Ready: Roystar/evolai-qwen2.5-1.5b@47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1
2026-05-24 10:49:01     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:49:01     Loss 3.1026 | Size ×0.50 | Think 3.1026 | ThinkGain 0 (+0.4547) | Flow
2026-05-24 10:49:01 0.2831 | KL 1.8911 | NextKL 2.2959 | SideQ 0% | Score 0.0000 (38.4s)
2026-05-24 10:49:01     Gate FAIL | Improve same SHA cur=1.8911 req<=1.8533 prev=1.8911 | Consist ok
2026-05-24 10:49:01 ema_cur=2.3750 ema_next=2.3557 ratio=0.992 max<=1.20
2026-05-24 10:49:03   Evicted cached model:
2026-05-24 10:49:03 mihai-777/evolai-mamba2-0p47b@7b6564c9a46f602702c260185aa43867f321dee7
2026-05-24 10:49:03   [10/50] UID 82 | clear-blue-sky/evolai-reborn-tfm-003 @
2026-05-24 10:49:03 ee61abb738c3d06872e7ee8a2c59c7287fbc632c | hotkey 5EtDxpyqHywK…
2026-05-24 10:49:03     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:49:03    Downloading Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d…
2026-05-24 10:49:03     Fetched 20 texts (20 indices)
2026-05-24 10:49:04     Loaded (local prefetch)
2026-05-24 10:49:05     Model 0.46B → batch=512, seq=16384
2026-05-24 10:49:06    Ready: Lin2es/evolai-tfm-01o@d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d
2026-05-24 10:49:43     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:35
2026-05-24 10:49:43     Loss 3.8607 | Size ×0.50 | Think 3.8607 | ThinkGain 0 (+0.4614) | Flow
2026-05-24 10:49:43 0.1127 | KL 2.1181 | NextKL 2.0170 | SideQ 0% | Score 0.0000 (38.2s)
2026-05-24 10:49:43     Gate FAIL | Improve FAIL cur=2.1181 req<=2.0795 prev=2.1219 | Consist ok
2026-05-24 10:49:43 ema_cur=1.8841 ema_next=1.9156 ratio=1.017 max<=1.20
2026-05-24 10:49:45   Evicted cached model:
2026-05-24 10:49:45 clear-blue-sky/evolai-reborn-tfm-002@445516ade25ae580764f845da0631604e1f2d573
2026-05-24 10:49:45   [11/50] UID 55 | Roystar/evolai-qwen2.5-1.5b @
2026-05-24 10:49:45 47e6a605a62ff328096c1d7bd160b8eaf9ec5ff1 | hotkey 5DhRJtUeVA6P…
2026-05-24 10:49:45     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:49:45     Fetched 20 texts (20 indices)
2026-05-24 10:49:45    Downloading
2026-05-24 10:49:45 clear-blue-sky/evolai-reborn-tfm-001@c9f7f10bd22cb9bfaed57700fbfa673f28f7191a…
2026-05-24 10:49:47     Loaded (local prefetch)
2026-05-24 10:49:48     ⚠ Vocab incompatible (model=151936 < ref=248077) — skipping
2026-05-24 10:49:50   [12/50] UID 77 | Lin2es/evolai-tfm-01o @
2026-05-24 10:49:50 d5af8d4f7543ee9e09ef3f668a29f2e09daeea8d | hotkey 5GQydjNVEhMb…
2026-05-24 10:49:50     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:49:50     Fetched 20 texts (20 indices)
2026-05-24 10:49:50    Ready:
2026-05-24 10:49:50 clear-blue-sky/evolai-reborn-tfm-001@c9f7f10bd22cb9bfaed57700fbfa673f28f7191a
2026-05-24 10:49:50    Downloading Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600…
2026-05-24 10:49:51     Loaded (local prefetch)
2026-05-24 10:49:52     Model 0.46B → batch=512, seq=16384
2026-05-24 10:49:53    Ready: Lin2es/evolai-tfm-03o@2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600
2026-05-24 10:50:25     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:31
2026-05-24 10:50:26     Loss 2.4276 | Size ×0.50 | Think 2.4276 | ThinkGain 0 (+0.4378) | Flow
2026-05-24 10:50:26 0.0000 | KL 2.8855 | NextKL 2.5148 | SideQ 0% | Score 0.0000 (33.9s)
2026-05-24 10:50:26     Gate FAIL | Improve same SHA cur=2.8855 req<=2.8277 prev=2.8855 | Consist ok
2026-05-24 10:50:26 ema_cur=2.6250 ema_next=2.6009 ratio=0.991 max<=1.20
2026-05-24 10:50:27   Evicted cached model:
2026-05-24 10:50:27 mrthor102/evolai-tfm-super-001@385ae8ed8a60a825e35a4eeb1f76f948662ae0e2
2026-05-24 10:50:27   [13/50] UID 62 | clear-blue-sky/evolai-reborn-tfm-001 @
2026-05-24 10:50:27 c9f7f10bd22cb9bfaed57700fbfa673f28f7191a | hotkey 5EjjVuNJsjqP…
2026-05-24 10:50:27     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:50:27     Fetched 20 texts (20 indices)
2026-05-24 10:50:27    Downloading Radiant28/evolai-1p5b@e351598db6d77f85b5081768df04d37c132750f0…
2026-05-24 10:50:29     Loaded (local prefetch)
2026-05-24 10:50:29     Model 0.46B → batch=512, seq=16384
2026-05-24 10:50:34    Ready: Radiant28/evolai-1p5b@e351598db6d77f85b5081768df04d37c132750f0
2026-05-24 10:51:08     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 10:51:08     Loss 3.0363 | Size ×0.50 | Think 3.0363 | ThinkGain 0 (+0.4572) | Flow
2026-05-24 10:51:08 0.0492 | KL 1.7508 | NextKL 1.7523 | SideQ 0% | Score 0.0000 (38.7s)
2026-05-24 10:51:08     Gate FAIL | Improve FAIL cur=1.7508 req<=1.7046 prev=1.7394 | Consist ok
2026-05-24 10:51:08 ema_cur=1.9350 ema_next=1.9018 ratio=0.983 max<=1.20
2026-05-24 10:51:10   Evicted cached model:
2026-05-24 10:51:10 clear-blue-sky/evolai-reborn-tfm-008@0ef35718add6719e5183c735af3f1f6034c10b7e
2026-05-24 10:51:11   [14/50] UID 79 | Lin2es/evolai-tfm-03o @
2026-05-24 10:51:11 2fcb3445759b5cb5d5d6a9be9e5731f72cc0f600 | hotkey 5D4eNqXRjWmX…
2026-05-24 10:51:11     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:51:11    Downloading galuis116/evolai-future@5f3808c2d4773a03c3ac1eaf8e8daff12986c528…
2026-05-24 10:51:11     Fetched 20 texts (20 indices)
2026-05-24 10:51:12     Loaded (local prefetch)
2026-05-24 10:51:12     Model 0.46B → batch=512, seq=16384
2026-05-24 10:51:15    Ready: galuis116/evolai-future@5f3808c2d4773a03c3ac1eaf8e8daff12986c528
2026-05-24 10:51:51     Loss eval ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80/80 100% 0:00:36
2026-05-24 10:51:52     Loss 2.5224 | Size ×0.50 | Think 2.5224 | ThinkGain 0 (+0.4622) | Flow
2026-05-24 10:51:52 0.0094 | KL 2.4695 | NextKL 2.5868 | SideQ 0% | Score 0.0000 (39.3s)
2026-05-24 10:51:52     Gate FAIL | Improve same SHA cur=2.4695 req<=2.4201 prev=2.4695 | Consist ok
2026-05-24 10:51:52 ema_cur=2.4323 ema_next=2.4499 ratio=1.007 max<=1.20
2026-05-24 10:51:53   Evicted cached model:
2026-05-24 10:51:53 clear-blue-sky/evolai-reborn-tfm-005@93513b7b277ea3f3e5b5a4a60f1ae4c88d9c2967
2026-05-24 10:51:54   [15/50] UID 43 | Radiant28/evolai-1p5b @
2026-05-24 10:51:54 e351598db6d77f85b5081768df04d37c132750f0 | hotkey 5HSz4knZnWHY…
2026-05-24 10:51:54     Challenge: evolai/universal_qa(20 idx)
2026-05-24 10:51:54     Fetched 20 texts (20 indices)
2026-05-24 10:51:54    Downloading
2026-05-24 10:51:54 mihai-777/evolai-tfm-1p5b@594894f806fb4c014675d89aad14f1c68976d52c…