## Buridan UI 내보내기(Export) 시스템 문서 (한국어)

Buridan UI의 내보내기 시스템을 이해하고 수정하기 위한 종합 가이드입니다.

## 개요

이 내보내기 시스템은 Buridan UI 애플리케이션을 위해 라우트, 컴포넌트, 페이지를 동적으로 생성하는 모듈형 구성 기반 아키텍처입니다. 주요 컴포넌트 유형은 다음과 같습니다.

- Pantry 컴포넌트: `buridan_ui/pantry/` 경로의 UI 컴포넌트
- Chart 컴포넌트: `buridan_ui/charts/` 경로의 차트 시각화 컴포넌트

## 아키텍처

### 핵심 클래스

```
ExportConfig          → 중앙화된 설정/구성
├── ComponentConfig   → 개별 컴포넌트/차트 구성
├── RouteConfig       → 정적 라우트 구성
└── 개발 모드         → 환경 변수 기반 필터링

SourceRetriever       → 소스 코드 검색 전략
├── get_pantry_source()
└── get_chart_source()

ExportFactory         → 내보내기 함수 생성
├── create_pantry_export()
└── create_chart_export()

ExportGenerator       → 내보내기 컬렉션 생성
├── generate_pantry_exports()
└── generate_chart_exports()

RouteManager          → 라우트 필터링 처리
└── filter_routes()

ApplicationExporter   → 오케스트레이션 엔트리포인트
└── export_app()      → 진입점
```

## 구성(Configuration)

### 새 컴포넌트 추가

#### 1. Pantry 컴포넌트

```python
# ExportConfig._init_configurations() 내부
self.COMPONENTS = {
    "your_component": ComponentConfig(
        versions=range(1, 4),  # 버전 1, 2, 3
        func_prefix="your_component",  # 함수 이름 접두사
        flexgen_url="https://...",     # 선택(옵션) FlexGen URL
    ),
    # ... 기존 컴포넌트들
}
```

#### 2. Chart 컴포넌트

```python
# ExportConfig._init_configurations() 내부
self.CHARTS = {
    "your_chart": ComponentConfig(
        versions=[1, 2, 5],  # 특정 버전 지정
        func_prefix="your_chart",
        flexgen_url="https://...",
        has_api_reference=True,  # API 문서 생성 포함
    ),
    # ... 기존 차트들
}
```

### 정적 라우트 추가

```python
# ExportConfig._init_getting_started_routes() 내부
from your_module import your_component

self.STATIC_ROUTES = [
    RouteConfig(
        path="/your-path",
        component=your_component,
        title="Your Page Title - Buridan UI"
    ),
    # ... 기존 라우트들
]
```

## 파일 구조 요구사항

### 컴포넌트 파일

컴포넌트 파일은 다음 구조를 따라야 합니다:

```
buridan_ui/pantry/your_component/
├── v1.py
├── v2.py
└── v3.py
```

각 버전 파일은 다음과 같이 함수를 내보내야 합니다:

```python
# buridan_ui/pantry/your_component/v1.py
def your_component_v1():
    return rx.div("Your component content")
```

### 함수 명명 규칙

- 파일: `v{version}.py`
- 함수: `{func_prefix}_v{version}`

예시:
- 파일: `v1.py` → 함수: `card_v1()`
- 파일: `v2.py` → 함수: `barchart_v2()`

## 개발 모드(Development Mode)

### 환경 변수

```bash
# 개발 모드 활성화
export BURIDAN_DEV_MODE=true

# 특정 컴포넌트 선택(쉼표 구분)
export BURIDAN_COMPONENTS=cards,buttons,forms

# 특정 차트 선택
export BURIDAN_CHARTS=bar,line,pie
```

### 개발 모드 동작

- 선택 없음: 모든 컴포넌트 포함
- 일부 선택: 선택된 항목만 포함
- 혼합 선택: 선택된 카테고리의 항목만 포함
- 카테고리 제외: 다른 카테고리만 선택된 경우, 선택되지 않은 카테고리는 제외

## 사용 예시

### 기본 사용

```python
# 메인 앱 파일
from src.export_system import export_app

app = rx.App()
export_app(app)  # 모든 처리를 담당
```

### 라우트 필터링(별도 사용 시)

```python
from src.export_system import filter_routes

# 개발 설정에 따른 라우트 필터링
filtered_routes = filter_routes(your_routes_list)
```

## 커스터마이즈

### 맞춤형 그리드 레이아웃

```python
# ExportConfig._init_configurations() 내부
self.GRID_CONFIGS = {
    "your_component": {
        "columns": 2,
        "spacing": "4",
        # responsive_grid의 인자들
    }
}
```

### 맞춤형 소스 검색

특수한 소스 처리 방식이 필요하다면:

```python
# SourceRetriever 클래스 내부
@staticmethod
def get_custom_source(directory: str, filename: str) -> str:
    """맞춤 소스 검색 로직."""
    # 사용자 정의 로직
    return source_code
```

그리고 해당 팩토리 메서드에서 이를 사용하도록 수정합니다.

### 맞춤형 Export 로직

특별한 내보내기가 필요할 때:

```python
# ExportFactory 클래스 내부
@staticmethod
def create_custom_export(directory: str, config: ComponentConfig, version: int) -> Callable:
    """맞춤 Export 함수 생성."""
    # 사용자 정의 로직
    pass
```

## 자주 하는 작업

### 새 컴포넌트 유형 추가

1. `ExportConfig._init_configurations()`에 구성 추가
2. `ExportConfig`에 필터링 로직 추가(예: `should_include_*` 메서드)
3. 필요 시 `SourceRetriever`에 소스 검색 로직 추가
4. `ExportFactory`에 내보내기용 팩토리 메서드 추가
5. `ExportGenerator`에 생성 메서드 추가
6. `ApplicationExporter._add_dynamic_routes()`에서 라우트 관리 업데이트

### 컴포넌트 버전 변경

```python
# range(1, 4) → range(1, 6)로 변경
"your_component": ComponentConfig(
    versions=range(1, 6),  # v4, v5 추가
    func_prefix="your_component",
)
```

### FlexGen URL 추가

```python
"your_component": ComponentConfig(
    versions=range(1, 4),
    func_prefix="your_component",
    flexgen_url="https://reflex.build/gen/your-gen-id/",
)
```

### API 문서 활성화

```python
# 현재 차트에만 적용
"your_chart": ComponentConfig(
    versions=range(1, 4),
    func_prefix="your_chart",
    has_api_reference=True,  # API 문서 추가
)
```

## 트러블슈팅

### 흔한 문제들

1. Import 에러: 파일 구조와 함수 명명을 확인하세요.
2. 라우트 누락: 라우트 구성과 개발 모드 설정을 확인하세요.
3. 소스 누락: 소스 검색 메서드에서 파일 경로를 확인하세요.
4. 버전 불일치: 버전 범위가 실제 파일과 일치하는지 확인하세요.

### 디버그 모드

`BURIDAN_DEV_MODE=true`일 때 시스템은 다음과 같이 디버그 정보를 출력합니다:

```
Development mode: Enabled
Selected components: cards, buttons
Selected charts: bar, line
```

### 에러 메시지 예시

```
Failed to import card_v1 from src.pantry.cards.v1: No module named 'buridan_ui.pantry.cards.v1'
```

## 모범 사례

1. 일관된 명명: `{prefix}_v{version}` 규칙을 따르세요.
2. 버전 관리: 연속 버전은 range, 특정 버전은 list를 사용하세요.
3. 구성 우선: 파일을 추가하기 전에 구성을 먼저 업데이트하세요.
4. 개발 모드 테스트: 개별 컴포넌트 테스트에 개발 모드를 활용하세요.
5. 변경 사항 문서화: 새로운 패턴을 추가할 때 이 문서를 업데이트하세요.

## 마이그레이션 가이드

### 기존 시스템에서 이전하기

기존 시스템에서 마이그레이션할 때:

1. 구성을 `ComponentConfig` 인스턴스로 이동
2. 새 규칙에 맞도록 함수명 업데이트
3. 정적 라우트를 `STATIC_ROUTES` 구성으로 이동
4. 공개 API를 사용하도록 import 업데이트
5. 개발 모드로 충분히 테스트

### 레거시 컴포넌트 추가

표준 패턴을 따르지 않는 컴포넌트의 경우 다음이 필요할 수 있습니다:

1. 맞춤 소스 검색 메서드 작성
2. 맞춤 Export 팩토리 메서드 작성
3. 구성에서 특수 케이스 처리

이 시스템은 관심사의 분리를 유지하면서도 유연하고 확장 가능하도록 설계되었습니다.
